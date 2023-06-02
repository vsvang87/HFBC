from flask import Flask, jsonify, render_template, redirect, session,request,flash
from model import db, Member, Event, connect_to_db
import crud

app = Flask(__name__)
app.secret_key = 'SECRETS'

#----------------------------Home Page------------------------------------#
@app.route('/')
def home():

    return render_template('index.html')

#----------------------------Login-----------------------------------------#
@app.route('/login')
def login():

    return render_template("login.html")

#---------------------------Login Post-----------------------------------#
@app.route('/login', methods=["POST"])
def user_login():
    
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_member_by_email(email)

    if not user or user.password != password:
        flash("Incorrect username, email or password", "error")
        return redirect("/login")
    else:
        session['user_email'] = user.email
        flash("Login Successful", "success")
        return redirect("/home")

#----------------------------New User Page----------------------------#
@app.route("/new_user")
def new_user():

    return render_template("new_user.html")


#--------------------------Create New User-----------------------------#
@app.route("/new_user", methods=["POST"])
def create_new_users():

    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_member_by_email("email")

    if user:
        flash("This account already exists")
        return redirect("/new_user")
    else:
        user = crud.create_member(first_name, last_name, email, password)
        db.session.add(user)
        db.session.commit()
        flash("Welcome, you have create new account successful")
        return redirect("/home")
   
#---------------------------Login Home Page-------------------#
@app.route("/home")
def user_login_home():

    return render_template("home.html")


@app.route("/event")
def event():

    return render_template("event.html")


@app.route("/host_event")
def host_event():

    return render_template("host_event.html")



#---------------------Log Out-------------------------------
@app.route("/logout")
def logout():

    session.clear()
    flash("Log out successful", "success")

    return redirect("/login")



#--------------------------------------------------------------#
if __name__ == '__main__':
    connect_to_db(app)
    app.run('0.0.0.0', debug=True)