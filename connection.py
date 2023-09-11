import mysql.connector

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='DdCya995142@4681',
            database='ssproject'
        )
        return connection
    except mysql.connector.Error as e:
        print("Error creating database connection:", str(e))
        return None
