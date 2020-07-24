from flask_sqlalchemy import SQLAlchemy
from flask import Flask,render_template,url_for,request,session,logging,redirect,flash


app = Flask(__name__)

@app.route("/", methods =['GET','POST'])

def login_user():

    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = "Invalid credentials. PLease try again."
            return redirect(url_for('login_error '))

        else:
            return redirect(url_for('home_page'))
    return render_template('login.html', error=error)

@app.route("/home")

def home_page():
    return render_template("index.html")

@app.route("/login_error")

def login_error():
    return render_template("login_error_message.html")

@app.route("/about")

def about():
    return render_template("about_page.html")

@app.route("/projects")

def projects():
    return render_template("projects.html")

@app.route("/sports")

def sports():
    return render_template("sports.html")

if __name__=="__main__":
    app.run(debug=True)


