from flask import Flask, render_template, redirect, url_for, request, session, flash, abort
from functools import wraps



app = Flask(__name__)

app.secret_key = 'mysecretkey'

@app.route("/home")

def home_page():
    session['attempt'] = 1
    return render_template("index.html")


@app.route("/", methods =['GET','POST'])

def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            attempt = int(session.get('attempt'))
            if attempt == 2:
                flash("This is your last chance")
                # attempt += 1
                # session['attempt'] = attempt
            if attempt == 3:
                flash('You have been logged out.')
                return render_template("login_error_message.html")
            else:
                attempt += 1
                session['attempt'] = attempt
                error = 'Invalid Credentials. Please try again'
        else:
            session['logged_in'] = True
            flash('You were logged in.')
            return redirect(url_for('home_page'))
    return render_template('login.html', error=error)



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


