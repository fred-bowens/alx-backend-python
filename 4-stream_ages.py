import mysql.connector

# Connect to the ALX_prodev database
def connect_to_prodev():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="ALX_prodev"
    )
def stream_user_ages():
    conn = connect_to_prodev()
    cursor = conn.cursor()
    cursor.execute("SELECT age FROM user_data")

    for (age,) in cursor:
        yield float(age)  # Ensure numeric type

    cursor.close()
    conn.close()
def calculate_average_age():
    total = 0
    count = 0

    for age in stream_user_ages():  # 1st loop
        total += age
        count += 1

    if count == 0:
        print("Average age of users: 0")
    else:
        average = total / count
        print(f"Average age of users: {average:.2f}")

if __name__ == "__main__":
    calculate_average_age()


import mysql.connector

# Configuration
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'your_password'
DB_NAME = 'ALX_prodev'
TABLE_NAME = 'user_data'

def stream_user_ages():
    """Generator that yields user ages one by one"""
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = connection.cursor()
        cursor.execute(f"SELECT age FROM {TABLE_NAME}")
        for (age,) in cursor:
            yield float(age)  # cast to float for average
        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return

def calculate_average_age():
    """Uses the age generator to calculate and print the average age"""
    total = 0
    count = 0
    for age in stream_user_ages():  # 1st and only loop
        total += age
        count += 1

    if count == 0:
        print("No users found.")
    else:
        average = total / count
        print(f"Average age of users: {average:.2f}")

# Execute
if __name__ == "__main__":
    calculate_average_age()
