from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\\\\n\\\\xec]/'

@app.route('/')
def index():
    return render_template('index.html', logged_in='username' in session)

@app.route('/menu')
def menu():
    connection = sqlite3.connect('poutines.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM menu")
    items = cursor.fetchall()
    connection.close()
    return render_template('menu.html', items=items, logged_in='username' in session)

@app.route('/menu_item')
def menu_item():
    poutine_id = request.args.get('id')
    connection = sqlite3.connect('poutines.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM menu WHERE id='{poutine_id}'")
    item = cursor.fetchone()
    connection.close()
    return render_template('menu_item.html', item=item)


@app.route('/user')
def user_profile():
    # This assumes the user is already logged in. Additional checks can be added if needed.
    return render_template('user.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    connection = sqlite3.connect('poutines.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'")
    user = cursor.fetchone()
    connection.close()

    if user:
        session['username'] = username
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
    app.run(debug=True, host='0.0.0.0', port=5000)