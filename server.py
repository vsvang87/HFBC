from flask import Flask, jsonify, render_template, redirect, session,request,flash
from model import db, User, Member, Event, connect_to_db
from flask_mail import Mail, Message

import crud
# import stripe

app = Flask(__name__)
app.secret_key = 'SECRETS'
# app.config["MAIL_SERVER"] = 'smtp.gmail.com'
# app.config["MAIL_PORT"] = 465
# app.config["MAIL_USERNAME"] = ' hfbc.milw@gmail.com'
# app.config["MAIL_PASSWORD"] = None
# app.config["MAIL_USE_TLS"] = False
# app.config["MAIL_USE_SSL"] = True
# mail = Mail(app)


# app.config['STRIPE_PUBLIC_KEY'] = 'pk_test_51NExkJJ4c4ZamGfp6EQd7l68VNd040Z9p9uo86X9O1WLdBmmpWoWVz0AVQZxwMYrEzPOiaGQaWDsXsl7CdmwvxjW00LHwa6iEZ'
# app.config['STRIPE_SECRET_KEY'] = 'sk_test_51NExkJJ4c4ZamGfpZ9jw4LLvtqckTvIZ1Rw8aYUIa5YwiAadabChXubwhHgsQXgoum1mxTQ9JQ0JNdubZcTo2W9d00GJAgYPpX'
# stripe.api_key = app.config['STRIPE_SECRET_KEY']

#----------------------------Home Page------------------------------------#
@app.route('/')
def index():

    events = Event.query.all()

    return render_template('index.html', events=events)

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
        session['user_email'] = user.email
        session['user_id'] = user.user_id
        db.session.add(user)
        db.session.commit()
        flash("Welcome, you have create new account successful")
        return redirect("/home")
   
#---------------------------Login Home Page-------------------#
@app.route("/home")
def user_login_home():

    email = session['user_email']
    users = crud.get_user_by_email(email)

    user_id = session["user_id"]
    members = crud.get_user_by_id(user_id)

    return render_template("home.html", users=users, members=members)

#-------------------------Add Church Member-------------------#
@app.route("/home", methods=["POST"])
def create_member():

    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    address = request.form.get("address")
    city = request.form.get("city")
    state = request.form.get("state")
    zipcode = request.form.get("zipcode")
    phone = request.form.get("phone")
    house_hold = request.form.get("house_hold")

    user_email = session['user_email']
    user_id = session['user_id']

    if user_email is None:
        flash("Have to logged in to add member", "error")
        return redirect("/home")
    else:
        member = crud.create_member(first_name, last_name, email, address, city, state, zipcode, phone, house_hold,user_id)
        db.session.add(member)
        db.session.commit()
        flash("Member has been add successfully", "success")
        
    return redirect("/home")


#----------------------Host Event-----------------------#
@app.route("/host_event")
def event():

    events = Event.query.all()
    
    return render_template("host_event.html", events=events, )


@app.route("/host_event", methods=["POST"])
def host_event():

    title = request.form.get("title")
    start_date = request.form.get("start_datetime")
    end_date = request.form.get("end_datetime")
    description = request.form.get("description")

    user_email = session['user_email']
    user_id = session['user_id']

    if not user_email:
        flash("Have to logged in to host an event")
        return redirect("/host_event")
    else:
        event = crud.create_event(title, start_date, end_date, description, user_id)
        db.session.add(event)
        db.session.commit()
        flash("Event has been created successfully")

    return redirect("/host_event")

#---------------------------Update Event-----------------------------#
@app.route("/update_event/<int:event_id>", methods=["GET", "POST"])
def update_event(event_id):

    event_update = Event.query.filter(Event.event_id == event_id).first()

    if request.method == "POST":
        event_update.title = request.form.get("title")
        event_update.start_date = request.form.get("start_date")
        event_update.end_date = request.form.get("end_date")
        event_update.description = request.form.get("description")
        try:
            db.session.commit()
            flash("Update event successful", "success")
            return redirect("/host_event")
        except:
            return "Error, unable to update"
        
    else:
        return render_template("update_event.html", event_update=event_update)

#---------------------Delete Events------------------------#
@app.route("/delete_event/<event_id>", methods=["POST"])
def delete(event_id):
    
    user_email = session['user_email']
    if user_email is None:
        flash("You must logged in to delete a post", "error")
    else:
        event = Event.query.filter(Event.event_id == event_id).first()
        db.session.delete(event)
        db.session.commit()
        flash("Event has been deleted", "success")

    
    return redirect("/host_event")
#-------------------Give---------------------------#
@app.route("/give")
def give():
    
    return render_template("give.html" )

@app.route("/thanks")
def thanks():

    return redirect("/give")

#---------------------About----------------------------#
@app.route("/about")
def about():

    return render_template("about.html")

@app.route("/ministries")
def ministry():

    return render_template("ministries.html")

#--------------------Display All Members----------------#
@app.route("/all_members")
def all_members():

    email = session['user_email']
    user = crud.get_user_by_email(email)

    all_members = Member.query.all()

    return render_template("all_members.html", all_members=all_members, user=user)


#-------------------------Update Member----------------------------#
@app.route("/update_member/<int:member_id>", methods=["GET", "POST"])
def update_member(member_id):

    member_update = Member.query.filter(Member.member_id == member_id).first()

    if request.method == "POST":
        member_update.first_name = request.form.get("first_name")
        member_update.last_name = request.form.get("last_name")
        member_update.address = request.form.get("address")
        member_update.city = request.form.get("city")
        member_update.state = request.form.get("state")
        member_update.zipcode = request.form.get("zipcode")
        member_update.phone = request.form.get("phone")
        member_update.email = request.form.get("email")
        member_update.house_hold = request.form.get("house_hold")
        try:
            db.session.commit()
            return redirect("/all_members")
        except:
            return "Error, unable to update"
        
    else:
        return render_template("update_members.html", member_update=member_update)


#--------------------Delete Member----------------------------#
@app.route("/delete_member/<int:member_id>")
def delete_member(member_id):

    member_delete = Member.query.filter(Member.member_id == member_id).first()

    try:
        db.session.delete(member_delete)
        db.session.commit()
        flash("Member deleted successfully", "success")
        return redirect("/all_members")
    except:
        return "Error, could not delete member"
    
#----------------------Serve Form-------------------------#
@app.route("/serve_form")
def serve():

    return render_template("serve_form.html")

# @app.route("/serve_form", methods=["POST"])
# def serve_form():

#     first_name = request.args.get("first_name")
#     last_name = request.args.get("last_name")
#     email = request.args.get("email")
#     message = request.args.get("message")

#     if request.method == "POST":
#         msg = Message(sender=email, recipients=['hfbc.milw@gmail.com'])
#         msg.body = message
#         mail.send(msg)
#         return "Sent"

#     return redirect("serve_form.html")
   
#---------------------Log Out-------------------------------
@app.route("/logout")
def logout():

    session.clear()
    flash("Log out successful", "success")

    return redirect("/login")

#----------------------Formate Date---------------------------
@app.template_filter("datetime_format")
def datetime_format(value, format='%B'):

    return value.strftime(format)


@app.template_filter("time_format")
def time_format(value, time='%H'):

    return value.strftime(time)

#--------------------------------------------------------------#
if __name__ == '__main__':
    connect_to_db(app)
    app.run('0.0.0.0', debug=True)