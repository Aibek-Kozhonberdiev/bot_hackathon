import psycopg2
from config import CONNECT

# Database connection
conn = psycopg2.connect(
    host=CONNECT['host'],
    user=CONNECT['user'],
    password=CONNECT['password'],
    database=CONNECT['database']   
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