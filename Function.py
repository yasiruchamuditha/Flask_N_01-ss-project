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
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='DdCya995142@4681',
            database='ss'
        )
         
        #connection = create_connection()  # Replace this with your actual connection code
        if connection.is_connected():
            cursor = connection.cursor()
            hashed_password = md5_hash_password(password)
            query = "INSERT INTO users (email, userrole, password) VALUES (%s, %s, %s)"
            data = (email, userrole, hashed_password)  # Include 'userrole' in data
            cursor.execute(query, data)
            connection.commit()
            print("User account created successfully.")
            return True  # Return True if user creation is successful
    except mysql.connector.Error as e:
        print("Error creating user:", str(e))
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
    
    return False  # Return False if user creation failed


# Function to authenticate a user during sign-in
def authenticate_user(email, password):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='DdCya995142@4681',
            database='ss'
        )
           
        if connection.is_connected():
            cursor = connection.cursor()
            hashed_password = md5_hash_password(password)
            query = "SELECT * FROM users WHERE email = %s AND password = %s"
            data = (email, hashed_password)
            cursor.execute(query, data)
            user = cursor.fetchone()
            if user:
                print("Authentication successful. Welcome,", email)
                return True  # Return True if authentication is successful
            else:
                print("Authentication failed. Invalid email or password.")
                return False
    except Error as e:
        print("Error:", str(e))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
    
    return False  # Return False if authentication failed



# Function to authenticate a user during sign-in
def find_usertype(email):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='DdCya995142@4681',
            database='ss'
        )
           
        if connection.is_connected():
            cursor = connection.cursor()
            query = "SELECT userrole FROM users WHERE email = %s"
            data = (email,)
            cursor.execute(query, data)
            userrole  = cursor.fetchone()
            if userrole :
                userrole = userrole[0]  # Extract the user_type from the tuple
                print("User type found:", userrole)
                return userrole  # Return the user_type if found
            else:
                print("Email not found")
                return None  # Return None if email not found
    except Error as e:
        print("Error:", str(e))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
    
    return False  # Return False if authentication failed
