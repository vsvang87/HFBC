from flask import Flask, jsonify, render_template, redirect, session,request,flash
from model import db, User, Member, Event, connect_to_db
import crud


app = Flask(__name__)
app.secret_key = 'SECRETS'

app.config['STRIPE_PUBLIC_KEY'] = 'pk_test_51NExkJJ4c4ZamGfp6EQd7l68VNd040Z9p9uo86X9O1WLdBmmpWoWVz0AVQZxwMYrEzPOiaGQaWDsXsl7CdmwvxjW00LHwa6iEZ'
app.config['STRIPE_SECRET_KEY'] = 'sk_test_51NExkJJ4c4ZamGfpZ9jw4LLvtqckTvIZ1Rw8aYUIa5YwiAadabChXubwhHgsQXgoum1mxTQ9JQ0JNdubZcTo2W9d00GJAgYPpX'


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

    user = crud.get_user_by_email(email)

    if not user or user.password != password:
        flash("Incorrect username, email or password", "error")
        return redirect("/login")
    else:
        session['user_email'] = user.email
        session['user_id'] = user.user_id
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

    user = crud.get_user_by_email("email")

    if user:
        flash("This account already exists")
        return redirect("/new_user")
    else:
        user = crud.create_user(first_name, last_name, email, password)
        db.session.add(user)
        db.session.commit()
        flash("Welcome, you have create new account successful")
        return redirect("/home")
   
#---------------------------Login Home Page-------------------#
@app.route("/home")
def user_login_home():


    return render_template("home.html")

@app.route("/home", methods=["POST"])
def create_member():

    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    address = request.form.get("address")
    phone = request.form.get("phone")
    house_hold = request.form.get("house_hold")

    user_email = session['user_email']
    user_id = session['user_id']

    if user_email is None:
        flash("Have to logged in to add member", "error")
        return redirect("/home")
    else:
        member = crud.create_member(first_name, last_name, email, address, phone, house_hold,user_id)
        db.session.add(member)
        db.session.commit()
        flash("Member has been add successfully", "success")
        
    return redirect("/home")


#----------------------Host Event-----------------------#
@app.route("/host_event")
def event():

    return render_template("host_event.html")


@app.route("/host_event", methods=["POST"])
def host_event():

    start_date = request.form.get("start_datetime")
    end_date = request.form.get("end_datetime")
    description = request.form.get("description")

    user_id = session['user_id']

    if not user_id:
        flash("Have to logged in to host an event")
        return redirect("/host_event")
    else:
        event = crud.create_event(start_date, end_date, description, user_id)
        db.session.add(event)
        db.session.commit()
        flash("Event has been created successfully")

    return redirect("/host_event")

#-------------------Give---------------------------#
@app.route("/give")
def give():

    return render_template("give.html")

@app.foute("/thanks")
def thanks():

    return redirect("/give")

#---------------------About----------------------------#
@app.route("/about")
def about():

    return render_template("about.html")

@app.route("/ministries")
def ministry():

    return render_template("ministries.html")


@app.route("/all_members")
def all_members():

    return render_template("all_members.html")
#--------------------Search--------------------------#
# @app.route("/search/<query>", methods=["POST"])
# def search(query):

#     search = request.form.get("search")
#     cur.execute(f"")
#     search_query = []

#     for i in range(10):
#         search_query.append()

#     return render_template("search.html")


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