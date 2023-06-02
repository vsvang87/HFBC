from model import db,User, Member, Event, connect_to_db


def create_user(first_name, last_name, email, password):
    
    user = User(first_name=first_name, last_name=last_name, email=email, password=password)

    return user
#--------------------Create New Member--------------------#
def create_member(first_name, last_name, email, address, phone_number, house_hold, user_id, image="https://res.cloudinary.com/dha9labk1/image/upload/v1685577322/vven5uk7a6nmn0otakaj.jpg"):

    member = Member(first_name=first_name, last_name=last_name, email=email, address=address, phone_number=phone_number, image=image, house_hold=house_hold, user_id=user_id)

    return member

#--------------------Create Events--------------------------#
def create_event(start_date, end_date, description):
    event = Event(start_date=start_date, end_date=end_date, description=description)

    return event

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



if __name__ == '__main__':
    from server import app
    connect_to_db(app)