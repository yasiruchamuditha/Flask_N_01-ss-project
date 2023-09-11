from flask import Flask, render_template ,url_for

from Function import signinmethod

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

@app.route("/loginFunction")
def loginFunction():
    function = signinmethod(email,password)
    

if __name__=="__main__":
    app.run(debug=True)