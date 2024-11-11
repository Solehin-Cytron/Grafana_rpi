import time
import random
import mysql.connector

# Database connection details
db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="your_mysql_user",
    password="your_mysql_password",
    database="dummy"
)

cursor = db.cursor()

def update_data():
    # Fetch the current values of data_a, data_b, and data_c
    cursor.execute("SELECT data_a, data_b, data_c FROM dashboard_data ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()
    if row:
        data_a, data_b, data_c = row

        # Increment each value by a random amount between 2 and 5
        data_a += random.randint(2, 5)
        data_b += random.randint(2, 5)
        data_c += random.randint(2, 5)

        # Update the database with the new values
        cursor.execute("""
            UPDATE dashboard_data 
            SET data_a = %s, data_b = %s, data_c = %s 
            WHERE id = (SELECT id FROM dashboard_data ORDER BY id DESC LIMIT 1)
        """, (data_a, data_b, data_c))
        
        db.commit()
        print(f"Updated data_a to {data_a}, data_b to {data_b}, data_c to {data_c}")
    else:
        print("No data found in dashboard_data table.")

# Run the script every 60 seconds
while True:
    update_data()
    time.sleep(60)
