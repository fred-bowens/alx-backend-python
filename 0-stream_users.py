import mysql.connector

def connect_to_prodev():
    connection = mysql.connector.connect(
        host="localhost",  # Update this with your MySQL host
        user="root",  # Update this with your MySQL user
        password="password",  # Update this with your MySQL password
        database="ALX_prodev"  # The database you want to connect to
    )
    return connection

def stream_users():
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")  # Fetch all rows from the table

    for row in cursor:
        yield row

    cursor.close()
    connection.close()

if __name__ == "__main__":
    for user in stream_users():
        print(user)


import mysql.connector

# Configuration
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'your_password'
DB_NAME = 'ALX_prodev'
TABLE_NAME = 'user_data'

def stream_users():
    """Generator function to stream users from the database one by one"""
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = connection.cursor(dictionary=True)

        cursor.execute(f"SELECT * FROM {TABLE_NAME}")
        for row in cursor:
            yield row

        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return

# Example usage
if __name__ == "__main__":
    for user in stream_users():
        print(user)
