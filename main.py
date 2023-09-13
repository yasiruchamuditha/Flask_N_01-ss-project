from flask import Flask, render_template ,url_for ,request

from Function import authenticate_user 
from Function import create_user 


app = Flask(__name__)

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
    authenticate_user(email,password)


@app.route("/RegisterMethod", methods=['POST'])
def SignUpMethod():
    email = request.form.get('txtUSerEmail')
    userrole = request.form.get('User_Role')
    password = request.form.get('txtPassword')
    cpassword = request.form.get('txtConfirm_Password')

    if password==cpassword:
        create_user(email,userrole,password)

   


       

if __name__=="__main__":
    app.run(debug=True)