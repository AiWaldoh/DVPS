from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import MySQLdb 
from MySQLdb.cursors import DictCursor
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\\\\n\\\\xec]/'

# Database configuration
DB_CONFIG = {
    'host': os.getenv('MYSQL_HOST'),
    'user': os.getenv('MYSQL_USER'),
    'passwd': os.getenv('MYSQL_PASSWORD'),
    'db': os.getenv('MYSQL_DATABASE')
}

def get_db_connection():
    return MySQLdb.connect(**DB_CONFIG)

@app.route('/')
def index():
    return render_template('index.html', logged_in='username' in session)

@app.route('/menu')
def menu():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM menu")
    items = cursor.fetchall()
    connection.close()
    return render_template('menu.html', items=items, logged_in='username' in session)

@app.route('/api/update_user_info', methods=['POST'])
def update_user_info():
    data = request.json
    field = data.get('field')
    value = data.get('value')

    # Assuming you have the user's ID stored in the session
    user_id = session.get('user_id')

    if not user_id:
        return jsonify(success=False, message="User not logged in!")

    # Connect to database and update the specified field with the provided value
    connection = get_db_connection()
    cursor = connection.cursor()
    
    query = f"UPDATE users SET {field} = %s WHERE id = %s"
    cursor.execute(query, (value, user_id))
    connection.commit()
    connection.close()

    return jsonify(success=True, message="Data updated!")

@app.route('/menu_item')
def menu_item():
    poutine_id = request.args.get('id')
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM menu WHERE id='{poutine_id}'")  # Vulnerable code
    item = cursor.fetchone()
    connection.close()
    return render_template('menu_item.html', item=item)

@app.route('/user/')
def user_profile():
    user_id = request.args.get('id')
    connection = get_db_connection()
    cursor = connection.cursor(DictCursor)

    # Using the f-string directly with the query can make it susceptible to SQL Injection.
    cursor.execute(f"SELECT * FROM users WHERE id='{user_id}'")  # Vulnerable code

    user = cursor.fetchone()
    print(type(user))
    connection.close()
    return render_template('user_profile.html', user=user)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'")  # Vulnerable code
    user = cursor.fetchone()
    connection.close()

    if user:
        session['username'] = username
        session['user_id'] = user[0]  # Assuming the 'id' column is the first column in your query
        flash(f"Welcome back, {username}!")
        return redirect(url_for('index'))
    else:
        flash("Invalid credentials!")
        return redirect(url_for('index'))



@app.route('/logout')
def logout():
    session.pop('username', None)
    flash("You have successfully logged out!")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
