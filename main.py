from flask import Flask, flash, render_template ,url_for ,request 

from Function import authenticate_user 
from Function import create_user 
import secrets

secret = secrets.token_urlsafe(32)


app = Flask(__name__)
app.secret_key = secret




@app.route("/")
def index():
    return render_template('Home.html')

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
        flash('Login successful!', 'success')
        # Redirect to the HTML page or route where you want to display the feedback message
        return render_template('/Home.html')
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
        
    
    
       

if __name__=="__main__":
    app.run(debug=True)