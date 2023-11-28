#oracle free doesnt support the security at multiple levels, so this 
#code is useless.

from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import MySQLdb 
from MySQLdb.cursors import DictCursor
from dotenv import load_dotenv
import os
load_dotenv()
import oracledb
# Function to get database connection
def get_oracle_db_connection():
    # Replace with your actual database connection details
    dsn = oracledb.makedsn('35.192.183.99', '1521', service_name='FREEPDB1')
    conn = oracledb.connect(user='system', password=os.getenv("ORACLE_PASSWORD"), dsn=dsn)
    return conn

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\\\\n\\\\xec]/'

# Database configuration
DB_CONFIG = {
    'host': os.getenv('MYSQL_HOST'),
    'user': os.getenv('MYSQL_USER'),
    'passwd': os.getenv('MYSQL_PASSWORD'),
    'db': os.getenv('MYSQL_DATABASE')
}

def get_mysql_db_connection():
    return MySQLdb.connect(**DB_CONFIG)

@app.route('/')
def index():
    return render_template('index.html', logged_in='username' in session)

@app.route('/menu')
def menu():
    connection = get_mysql_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM menu")
    items = cursor.fetchall()
    connection.close()
    return render_template('menu.html', items=items, logged_in='username' in session)


@app.route('/menu_item')
def menu_item():
    poutine_id = request.args.get('id')
    connection = get_oracle_db_connection()
    cursor = connection.cursor()

    # Intentionally vulnerable code
    cursor.execute(f"SELECT * FROM POUTINE_SHOP.MENU WHERE ID = '{poutine_id}'")  # Adjust the table name as necessary
    item = cursor.fetchone()
    connection.close()

    return render_template('menu_item.html', item=item)

@app.route('/user/')
def user_profile():
    user_id = request.args.get('id')
    connection = get_oracle_db_connection()
    cursor = connection.cursor()

    # Intentionally vulnerable query
    query = f"SELECT * FROM POUTINE_SHOP.USERS WHERE USER_ID = '{user_id}'"  # Adjust the table name as necessary
    cursor.execute(query)

    user = cursor.fetchone()
    # connection.close()

    # Convert the row to a dictionary keyed by column name if 'user' is not None
    if user:
        columns = [col[0] for col in cursor.description]
        user = dict(zip(columns, user))

    return render_template('user_profile.html', user=user)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    connection = get_oracle_db_connection()
    cursor = connection.cursor()
    
    # Intentionally vulnerable code
    cursor.execute(f"SELECT * FROM POUTINE_SHOP.USERS WHERE USERNAME = '{username}' AND PASSWORD = '{password}'")
    
    user = cursor.fetchone()
    connection.close()

    if user:
        # Assuming the 'id' column is the first column in your query
        session['username'] = username
        session['user_id'] = user[0]
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
    app.run(debug=True, host='0.0.0.0', port=5002)
