import mysql.connector
import hashlib
from mysql.connector import Error


# Function to create a database connection
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
    

# Function to hash a password using MD5
def md5_hash_password(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

# Function to create a new user account
def create_user(email, userrole, password):
    try:
        if connection.is_connected():
            cursor = connection.cursor()
            hashed_password = md5_hash_password(password)
            query = "INSERT INTO users (email,userrole, password) VALUES (%s,%s, %s)"
            data = (email, hashed_password)
            cursor.execute(query, data)
            connection.commit()
            print("User account created successfully.")
    except Error as e:
        print("Error creating user:", str(e))

# Function to authenticate a user during sign-in
def authenticate_user(email, password):
    try:
        if connection.is_connected():
            cursor = connection.cursor()
            hashed_password = md5_hash_password(password)
            query = "SELECT * FROM users WHERE email = %s AND password = %s"
            data = (email, hashed_password)
            cursor.execute(query, data)
            user = cursor.fetchone()
            if user:
                print("Authentication successful. Welcome,", email)
            else:
                print("Authentication failed. Invalid email or password.")
    except Error as e:
        print("Error:", str(e))

# login program loop
def signinmethod(email,password):
    try:
        connection = create_connection()  # Call create_connection from the imported module
        if connection:
            while True:
                authenticate_user(connection, email, password)

    finally:
        if connection and connection.is_connected():
            connection.close()


# Main program loop
def signupmethod(email,userrole,password):
    try:
        connection = create_connection()  # Call create_connection from the imported module
        if connection:
            while True:
                create_user(connection, email,userrole, password)
                
    finally:
        if connection and connection.is_connected():
            connection.close()