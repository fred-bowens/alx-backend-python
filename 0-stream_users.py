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
