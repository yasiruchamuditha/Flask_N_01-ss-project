from flask import Flask, flash, render_template ,url_for ,request ,session
from Function import authenticate_user 
from Function import create_user 
from Function import find_usertype 
from Function import find_user_email 
from Encryption import encrypt
from Decryption import decrypt
import secrets

# @author Yasiru
# contact me: https://linktr.ee/yasiruchamuditha for more information.

#create secreat key
secret = secrets.token_urlsafe(32)

app = Flask(__name__)
app.secret_key = secret

#route for load index page
@app.route("/")
def index():
    return render_template('Home.html')

#route for load home page
@app.route("/home")
def home():
    return render_template('Home.html')

#route for load register page
@app.route("/register")
def register():
    return render_template('Register.html')

#route for load login page
@app.route("/login")
def login():
    return render_template('Login.html')

#route for load sendMessage page
@app.route("/sendmessage")
def sendMessage():
    return render_template('SendMessage.html')

#route for login form action    
@app.route("/LoginMethod", methods=['POST'])
def LoginMethod():
    email = request.form.get('txtUSerEmail')
    password = request.form.get('txtPassword')
    if authenticate_user(email, password):
        #check user role of email
        userrole=find_usertype(email)
        print('usertype checked in main body.',userrole)
        if userrole is not None:
            #decrypt message method
            decrypted_Message = decrypt(userrole)
            if decrypted_Message is not None:
               flash('Decryption is  successful!', 'success')
               print("Decrypted Message in succesful in main body:", decrypted_Message)
               # Pass the decrypted_Message to the template
               return render_template('DisplayMessage.html', decrypted_Message=decrypted_Message)
            else:
               flash('Decryption failed.', 'error')
               print("Decrypted Message in failed in main body:")
               # Redirect to the HTML page to display the feedback message
               return render_template('/Login.html')
   
        else:
            flash('Login failed. Invalid email or password.', 'error')
            # Redirect to the HTML page to display the feedback message
            return render_template('/Login.html') 
    else:
        flash('Login failed. Invalid email or password.', 'error')
        # Redirect to the HTML page to display the feedback message
        return render_template('/Login.html')

    
#route for registration form action  
@app.route("/RegisterMethod", methods=['POST'])
def SignUpMethod():
    email = request.form.get('txtUSerEmail')
    userrole = request.form.get('User_Role')
    password = request.form.get('txtPassword')
    cpassword = request.form.get('txtConfirm_Password')

    if password == cpassword:
        foundEmail = find_user_email(email)
        if foundEmail is None:
            if create_user(email, userrole, password):
                flash('Registration successful! Please login.', 'success')
                # Redirect to the HTML page to display the feedback message
                return render_template('/Login.html')
            else:
                flash('Registration failed. Please try again later.', 'error')
                # Redirect to the HTML page to display the feedback message
                return render_template('/Register.html')  
        else:
            flash('Registration failed. Already have Account under Email', 'error')
            # Redirect to the HTML page to display the feedback message 
            return render_template('/Register.html')   

    else:
        flash('Password and confirm password do not match. Please try again.', 'error')
    
    # Redirect to the HTML  to display the feedback message
    return render_template('/Register.html')
        

#route for sendMessage form action  
@app.route("/SendMessageMethod", methods=['POST'])
def MessageMethod():
    message = request.form.get('textareaMessage').encode()
    user_type = request.form.get('User_Role')
    print(message)
    print(user_type)
    #Check userrole and send encrypt method
    if encrypt(message,user_type):
        flash('Message encrypted and saved.', 'success')
    else:
        flash('Message encryption failed. Please Try Again later.', 'error')
      
    #Redirect to the HTML page  to display the feedback message
    return render_template('/SendMessage.html')
    
      

if __name__=="__main__":
    app.run(debug=True)