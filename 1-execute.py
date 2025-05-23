import sqlite3

class ExecuteQuery:
    def __init__(self, query, params=()):
        self.query = query
        self.params = params
        self.conn = None
        self.results = None
    
    def __enter__(self):
        self.conn = sqlite3.connect('users.db')
        cursor = self.conn.cursor()
        cursor.execute(self.query, self.params)
        self.results = cursor.fetchall()
        return self.results  # Return the results from __enter__
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.close()
        # Do not suppress exceptions
        return False

# Usage example
with ExecuteQuery("SELECT * FROM users WHERE age > ?", (25,)) as results:
    for row in results:
        print(row)
