import sqlite3

def create_and_populate_db():
    # Connect to the database (or create it if it doesn't exist)
    connection = sqlite3.connect('poutines.db')
    cursor = connection.cursor()

    # Check if the 'menu' table exists
    cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='menu' ''')

    # If the count is 0, then table doesn't exist
    if cursor.fetchone()[0] == 0:
        # Create the 'menu' table
        cursor.execute('''
            CREATE TABLE menu (
                id INTEGER PRIMARY KEY,
                name TEXT,
                price REAL,
                description TEXT,
                ingredients TEXT,
                image TEXT
            )
        ''')

        # Populate the table with dummy data
        cursor.executemany('''
            INSERT INTO menu (name, price, description, ingredients, image)
            VALUES (?, ?, ?, ?, ?)
        ''', [
            ('Classic Poutine', 7.99, 'Our classic poutine.', 'Fries, Gravy, Cheese Curds', 'classic.jpg'),
            ('Bacon Poutine', 9.99, 'Poutine with crispy bacon.', 'Fries, Gravy, Cheese Curds, Bacon', 'bacon.jpg'),
            # Add more dummy data as needed
        ])

    # Check if the 'users' table exists
    cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='users' ''')

    # If the count is 0, then table doesn't exist
    if cursor.fetchone()[0] == 0:
        # Create the 'users' table
        cursor.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                password TEXT
            )
        ''')

        # Populate the table with dummy users (with unencrypted passwords)
        cursor.executemany('''
            INSERT INTO users (username, password)
            VALUES (?, ?)
        ''', [
            ('admin', 'password123'),
            ('guest', 'guestpass'),
            ('kevin', 'sUP3R_S3KUre___P@55W0RDZ2023&&&&&&&&&&&&&&&&&&&&&&&&&'),
            ('pmm', 'pmmpassword')
        ])


    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_and_populate_db()