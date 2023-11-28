#simple file to test oracle connection

import oracledb

def test_database_connection():
    username = 'system'  # Or another user with required privileges
    password = ''  # Replace with the actual password
    dsn = 'localhost/FREEPDB1'  # Update with your DSN for the Oracle database

    try:
        # Attempt to establish a database connection
        connection = oracledb.connect(user=username, password=password, dsn=dsn)
        print("Successfully connected to the database.")

    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"Database error occurred: {error.code} - {error.message}")

    finally:
        # Clean up and close the database connection
        if 'connection' in locals():
            connection.close()

if __name__ == "__main__":
    print("Starting the script...")
    test_database_connection()
    print("Script finished.")
