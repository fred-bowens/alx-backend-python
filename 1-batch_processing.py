import mysql.connector

def connect_to_prodev():
    connection = mysql.connector.connect(
        host="localhost",  # Update this with your MySQL host
        user="root",  # Update this with your MySQL user
        password="password",  # Update this with your MySQL password
        database="ALX_prodev"  # The database you want to connect to
    )
    return connection

def stream_users_in_batches(batch_size):
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")  # Fetch all rows from the table

    batch = []
    for row in cursor:
        batch.append(row)
        if len(batch) == batch_size:
            yield batch
            batch = []  # Reset the batch after yielding
    if batch:  # Yield the remaining rows that don't fill a full batch
        yield batch

    cursor.close()
    connection.close()

def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):
        filtered_users = [user for user in batch if user['age'] > 25]
        for user in filtered_users:
            yield user  # Yield each filtered user one by one

if __name__ == "__main__":
    batch_size = 5  # Adjust batch size as needed
    for user in batch_processing(batch_size):
        print(user)
