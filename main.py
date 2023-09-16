from flask import Flask, flash, render_template ,url_for ,request ,session
from Function import authenticate_user 
from Function import create_user 
from Function import find_usertype 
from Encryption import encrypt
from Decryption import decrypt
import secrets

secret = secrets.token_urlsafe(32)


app = Flask(__name__)
app.secret_key = secret


@app.route("/")
def index():
    return render_template('SendMessage.html')

@app.route("/home")
def home():
    return render_template('Home.html')

@app.route("/register")
def register():
    return render_template('Register.html')

@app.route("/login")
def login():
    return render_template('Login.html')

@app.route("/sendmessage")
def sendMessage():
    return render_template('SendMessage.html')
    
@app.route("/LoginMethod", methods=['POST'])
def LoginMethod():
    email = request.form.get('txtUSerEmail')
    password = request.form.get('txtPassword')
    if authenticate_user(email, password):
        usertype=find_usertype(email)
        print('usertype checked in main body.',usertype)
        if usertype is not None:
            decrypted_Message = decrypt(usertype)
            if decrypted_Message is not None:
               flash('Decryption is  successful!', 'success')
               print("Decrypted Message in succesful in main body:", decrypted_Message)
               # Pass the decrypted_Message to the template
               return render_template('DisplayMessage.html', decrypted_Message=decrypted_Message)
            else:
               flash('Decryption failed.', 'error')
               print("Decrypted Message in failed in main body:")
               return render_template('/Login.html')
   
        else:
            flash('Login failed. Invalid email or password.', 'error')
            # Redirect to the HTML page or route where you want to display the feedback message
            return render_template('/Login.html') 
    else:
        flash('Login failed. Invalid email or password.', 'error')
        # Redirect to the HTML page or route where you want to display the feedback message
        return render_template('/Login.html')

    


@app.route("/RegisterMethod", methods=['POST'])
def SignUpMethod():
    email = request.form.get('txtUSerEmail')
    userrole = request.form.get('User_Role')
    password = request.form.get('txtPassword')
    cpassword = request.form.get('txtConfirm_Password')

    if password == cpassword:
        if create_user(email, userrole, password):
            flash('Registration successful!', 'success')
        else:
            flash('Registration failed. Please try again later.', 'error')
    else:
        flash('Password and confirm password do not match. Please try again.', 'error')
    
    # Redirect to the HTML page or route where you want to display the feedback message
    return render_template('/Login.html')
        


@app.route("/SendMessageMethod", methods=['POST'])
def MessageMethod():
    message = request.form.get('textareaMessage').encode()
    user_type = request.form.get('User_Role')
    print(message)
    print(user_type)

    if encrypt(message,user_type):
        flash('Message encrypted and saved.', 'success')
    else:
        flash('Message encryption failed. Please Try Again later.', 'error')
      
    # Redirect to the HTML page or route where you want to display the feedback message
    return render_template('/SendMessage.html')
    

       

if __name__=="__main__":
    app.run(debug=True)