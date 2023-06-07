from model import db,User, Member, Event, connect_to_db


def create_user(first_name, last_name, email, password):
    
    user = User(first_name=first_name, last_name=last_name, email=email, password=password)

    return user
#--------------------Create New Member--------------------#
def create_member(first_name, last_name, email, address, city, state, zipcode, phone_number, house_hold, user_id):

    member = Member(first_name=first_name, last_name=last_name, email=email, address=address, city=city, state=state, zipcode=zipcode, phone_number=phone_number, house_hold=house_hold, user_id=user_id)

    return member

#--------------------Create Events--------------------------#
def create_event(start_date, end_date, description, user_id):
    event = Event(start_date=start_date, end_date=end_date, description=description, user_id=user_id)

    return event


def get_user_by_firstname(first_name):

    return User.query.filter(User.first_name == first_name).first()
#-------------------Get Member_Id-------------------#
def get_member(member_id):

    return Member.query.filter(Member.member_id == member_id).all()

#-----------------------Get User Id-------------------------#
def get_user_by_id(user_id):

    return User.query.filter(User.user_id == user_id).first()

#-----------------------Get user email-------------------#
def get_user_by_email(email):
    
    return User.query.filter(User.email == email).first()

#------------------------Member Id-----------------------------------#
def get_member_by_id(member_id):
    
    return Member.query.filter(Member.user_id == member_id).all()

#-----------------------Get User Email-------------------------------#
def get_member_by_email(email):
    
    return Member.query.filter(Member.email == email).first()

#------------------------Get User Password--------------------------#
def get_member_by_password(password):

    return Member.query.filter(Member.password == password).first()

#------------------------Get Event---------------------------------#
def get_event(event_id):

    return Event.query.filter(Event.event_id == event_id).all()

#----------------------Update Image From Cloudinary----------#
# def update_img_url(image_url, user):

#     user.image_url = image_url

#     return image_url


if __name__ == '__main__':
    from server import app
    connect_to_db(app)