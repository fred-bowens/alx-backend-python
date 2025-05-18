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
