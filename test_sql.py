import psycopg2
from config import connect

# Database connection
conn = psycopg2.connect(
    host=connect['host'],
    user=connect['user'],
    password=connect['password'],
    database=connect['database']   
)

# Perform database operations
# For example, executing a SQL query
cur = conn.cursor()
cur.execute("SELECT * FROM users;")
results = cur.fetchall()
for row in results:
    print(row)

# Closing database connections
conn.close()