import mysql.connector

try:
    # Establish the connection
    mydb = mysql.connector.connect(
        host="localhost",          # Replace with your MySQL server host
        user="root",               # Replace with your MySQL username
        password="yourpassword",  # Replace with your MySQL password
        database=""                # Leave blank if no specific database is needed
    )

    # Check the connection
    if mydb.is_connected():
        print("Connected to MySQL server")
        print(f"MySQL Server Version: {mydb.get_server_info()}")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the connection
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
        print("Database connection closed")