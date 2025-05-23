import mysql.connector

# Connect to the ALX_prodev database
def connect_to_prodev():
    connection = mysql.connector.connect(
        host="localhost",        # Update with your DB host
        user="root",             # Update with your DB user
        password="password",     # Update with your DB password
        database="ALX_prodev"
    )
    return connection

def paginate_users(page_size, offset):
    conn = connect_to_prodev()
    cursor = conn.cursor(dictionary=True)
    
    query = "SELECT * FROM user_data LIMIT %s OFFSET %s"
    cursor.execute(query, (page_size, offset))
    results = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return results

def lazy_paginate(page_size):
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size  # Move to the next page

if __name__ == "__main__":
    for page in lazy_paginate(3):  # Change page_size as needed
        print(f"Fetched page with {len(page)} users:")
        for user in page:
            print(user)


import mysql.connector

# Configuration
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'your_password'
DB_NAME = 'ALX_prodev'
TABLE_NAME = 'user_data'

def paginate_users(page_size, offset):
    """
    Fetches a page of users starting at the given offset.
    Returns a list of user records.
    """
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = connection.cursor(dictionary=True)
        query = f"SELECT * FROM {TABLE_NAME} LIMIT %s OFFSET %s"
        cursor.execute(query, (page_size, offset))
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return []

def lazy_paginate(page_size):
    """
    Generator that yields pages of users one at a time.
    Only fetches data when needed, starting from offset 0.
    """
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size

# Example usage
if __name__ == "__main__":
    for page in lazy_paginate(3):  # One loop only
        for user in page:
            print(user)
