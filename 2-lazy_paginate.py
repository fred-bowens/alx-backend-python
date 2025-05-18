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
