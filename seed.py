import mysql.connector
import csv
import uuid

def connect_db():
    return mysql.connector.connect(
        host="localhost",  # Replace with your MySQL host if necessary
        user="root",  # Replace with your MySQL user
        password="password"  # Replace with your MySQL password
    )

def create_database(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    connection.commit()
    cursor.close()

def connect_to_prodev():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="ALX_prodev"
    )
    return connection

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id CHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL(5, 2) NOT NULL,
            INDEX (user_id)
        )
    """)
    connection.commit()
    cursor.close()

def insert_data(connection, data):
    cursor = connection.cursor()
    for row in data:
        cursor.execute("""
            INSERT INTO user_data (user_id, name, email, age) 
            SELECT %s, %s, %s, %s
            WHERE NOT EXISTS (SELECT 1 FROM user_data WHERE user_id = %s)
        """, (row['user_id'], row['name'], row['email'], row['age'], row['user_id']))
    connection.commit()
    cursor.close()

def load_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = []
        for row in reader:
            data.append({
                'user_id': str(uuid.uuid4()),  # Generate a UUID for each row
                'name': row['name'],
                'email': row['email'],
                'age': row['age']
            })
    return data
  
def stream_rows(connection):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")
    for row in cursor:
        yield row
    cursor.close()
  
    connection = connect_db()

    
    create_database(connection)
    
    connection = connect_to_prodev()

    
    create_table(connection)
    data = load_csv('user_data.csv')
    insert_data(connection, data)

    
    print("Streaming rows from the database:")
    for row in stream_rows(connection):
        print(row)

    
    connection.close()

if __name__ == '__main__':
    main()


 
python
Copy
Edit
import mysql.connector
from mysql.connector import errorcode
import pandas as pd
import uuid

# Configuration - adjust as needed
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'your_password'
DB_NAME = 'ALX_prodev'
TABLE_NAME = 'user_data'
CSV_FILE = 'user_data.csv'

def connect_db():
    """Connect to MySQL server (no database selected yet)"""
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
        print("Connected to MySQL server.")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        exit(1)

def create_database(connection):
    """Create database if not exists"""
    cursor = connection.cursor()
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        print(f"Database `{DB_NAME}` checked/created.")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
    cursor.close()

def connect_to_prodev():
    """Connect to the ALX_prodev database"""
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        print(f"Connected to database `{DB_NAME}`.")
        return connection
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        exit(1)

def create_table(connection):
    """Create the user_data table"""
    cursor = connection.cursor()
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        user_id CHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL(3,0) NOT NULL,
        INDEX (user_id)
    )
    """
    try:
        cursor.execute(create_table_query)
        print(f"Table `{TABLE_NAME}` checked/created.")
    except mysql.connector.Error as err:
        print(f"Failed creating table: {err}")
    cursor.close()

def insert_data(connection, data):
    """Insert data into the table if not exists"""
    cursor = connection.cursor()
    for index, row in data.iterrows():
        user_id = str(uuid.uuid4())
        name = row['name']
        email = row['email']
        age = row['age']
        # Check if email already exists
        cursor.execute(f"SELECT email FROM {TABLE_NAME} WHERE email = %s", (email,))
        if cursor.fetchone():
            print(f"Skipped duplicate email: {email}")
            continue
        cursor.execute(
            f"INSERT INTO {TABLE_NAME} (user_id, name, email, age) VALUES (%s, %s, %s, %s)",
            (user_id, name, email, age)
        )
    connection.commit()
    print("Data insertion complete.")
    cursor.close()

if __name__ == "__main__":
    # Read CSV
    try:
        data = pd.read_csv(CSV_FILE)
    except FileNotFoundError:
        print(f"CSV file '{CSV_FILE}' not found.")
        exit(1)

    # Steps
    conn = connect_db()
    create_database(conn)
    conn.close()

    prodev_conn = connect_to_prodev()
    create_table(prodev_conn)
    insert_data(prodev_conn, data)
    prodev_conn.close()
