import oracledb
import os
from dotenv import load_dotenv
load_dotenv()

# -- Log in as SYS or SYSTEM user
# -- Run the following SQL command to give POUTINE_SHOP a quota on the USERS tablespace

# ALTER USER POUTINE_SHOP QUOTA UNLIMITED ON USERS;

# Assuming you're using the SYSTEM user to connect
username = 'system'
password = 'P@ssw0rd'
dsn = 'localhost/FREEPDB1'  # Update with your DSN
def get_oracle_db_connection():
    # Replace with your actual database connection details
    dsn = oracledb.makedsn('35.192.183.99', '1521', service_name='FREEPDB1')
    conn = oracledb.connect(user='system', password=os.getenv("ORACLE_PASSWORD"), dsn=dsn)
    return conn
def insert_users():
    try:
        # Use global variables to establish the database connection
        connection = get_oracle_db_connection()
        cursor = connection.cursor()
        
        # Change the current schema to POUTINE_SHOP
        cursor.execute("ALTER SESSION SET CURRENT_SCHEMA = POUTINE_SHOP")
        
        # Insert user entries
        for i in range(1, 41):  # Adjust range for the number of users you want to create
            player_username = f'Player{i}'  # Create a unique username for each player
            # Execute the insert statement
            cursor.execute("""
                INSERT INTO Users (Username, Password) VALUES (:1, :2)
            """, [player_username, player_username])  # Username and password are the same
            
        # Commit the changes
        connection.commit()
        print("Users have been inserted successfully.")
        
    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"Database error occurred: {error.code} - {error.message}")
        
    finally:
        # Clean up the database resources
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()

def create_users_table():
    try:
        connection = get_oracle_db_connection()
        cursor = connection.cursor()

        # Change the current schema to POUTINE_SHOP
        cursor.execute("ALTER SESSION SET CURRENT_SCHEMA = POUTINE_SHOP")

        # Create users table
        cursor.execute("""
            CREATE TABLE users (
                user_id INT PRIMARY KEY,
                username VARCHAR2(50),
                password VARCHAR2(50),
                role VARCHAR(50)
            )
        """)

        # Create PoutineRecipes table
        cursor.execute("""
            CREATE TABLE PoutineRecipes (
                RecipeID INT PRIMARY KEY,
                RecipeDetails CLOB,
                SecurityLevel VARCHAR(50)
            )
        """)

        # Create sequence for user_id
        cursor.execute("""
            CREATE SEQUENCE users_seq
                START WITH 1
                INCREMENT BY 1
        """)

        # Create trigger for auto-incrementing user_id
        cursor.execute("""
            CREATE OR REPLACE TRIGGER users_bir 
            BEFORE INSERT ON users 
            FOR EACH ROW
            BEGIN
              SELECT users_seq.NEXTVAL
              INTO   :new.user_id
              FROM   dual;
            END;
        """)

        connection.commit()
        print("Tables and supporting objects have been created successfully.")

    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"Database error occurred: {error.code} - {error.message}")
        raise

    except Exception as e:
        print(f"An error occurred: {e}")
        raise

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()



if __name__ == "__main__":
    print("Starting the script...")
    create_users_table()
    insert_users()
    print("Script finished.")
