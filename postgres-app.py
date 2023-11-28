from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host=os.getenv('BOX_IP'),
                            database='postgres',
                            user=os.getenv('POSTGRES_USERNAME'),
                            password=os.getenv('POSTGRES_PASSWORD'))
    return conn

@app.route('/')
def index():
    return render_template('index.html', logged_in='username' in session)

@app.route('/menu')
def menu():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM poutine")
    items = cursor.fetchall()
    connection.close()
    return render_template('p_menu.html', items=items, logged_in='username' in session)

@app.route('/menu_item')
def menu_item():
    poutine_id = request.args.get('id')
    connection = get_db_connection()
    cursor = connection.cursor()

    # Vulnerable SQL query
    cursor.execute(f"SELECT * FROM poutine WHERE id='{poutine_id}'")
    item = cursor.fetchone()

    connection.close()
    return render_template('p_menu_item.html', item=item)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5005)
