import psycopg2
import random

# Connect to the database
conn = psycopg2.connect(
    host="your_host_name",
    database="your_database_name",
    user="your_username",
    password="your_password"
)
cursor = conn.cursor()

# Create the table
cursor.execute('''CREATE TABLE IF NOT EXISTS employee
                (emp_id SERIAL PRIMARY KEY,
                dept_id INTEGER,
                salary INTEGER,
                emp_name TEXT)''')

# Define the range of values for salary
min_salary = 500
max_salary = 1500

# Define the possible values for dept_id
dept_ids = [1, 2, 3]

# Define the number of rows to insert at a time
batch_size = 1000

# Generate the rows to insert
rows = [(i, random.choice(dept_ids), random.randint(min_salary, max_salary), f"Employee {i}") for i in range(1, 1000001)]

# Insert the rows in batches
for i in range(0, len(rows), batch_size):
    batch = rows[i:i+batch_size]
    cursor.executemany("INSERT INTO employee (dept_id, salary, emp_name) VALUES (%s, %s, %s)", [(r[1], r[2], r[3]) for r in batch])
    print(f"{i+batch_size} rows inserted.")

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Done.")
