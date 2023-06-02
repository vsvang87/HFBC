from model import db, Member, Event, connect_to_db


def create_member(first_name, last_name, email, password):
    
    member = Member(first_name=first_name, last_name=last_name, email=email, password=password)

    return member


def create_event(start_date, end_date, description):
    event = Event(start_date=start_date, end_date=end_date, description=description)

    return event


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