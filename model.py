from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False, unique=True)

    member = db.relationship("Member", back_populates="user")
    event = db.relationship("Event", back_populates="user")

    def __repr__(self):
        return f"<User user_id={self.member_id} first_name={self.first_name}>"


class Member(db.Model):
    
    __tablename__ = "members"

    member_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=True, unique=True)
    address = db.Column(db.String(50), nullable=True)
    city = db.Column(db.String(50), nullable=True)
    state = db.Column(db.String(50), nullable=True)
    zipcode = db.Column(db.Integer, nullable=True)
    phone_number = db.Column(db.String(20), nullable=True)
    house_hold = db.Column(db.Integer, nullable=True)
    # image_url = db.Column(db.String, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    user = db.relationship("User", back_populates="member")
    # event = db.relationship("Event", back_populates="member")

    def __repr__(self):
        return f"<Member member_id={self.member_id} first_name={self.first_name}>"
    
#------------------------------------Event Table------------------------#
class Event(db.Model):

    __tablename__ = "events"

    event_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=True)
    start_date = db.Column(db.DateTime, nullable=True)
    end_date = db.Column(db.DateTime, nullable=True)
    description = db.Column(db.String(500), nullable=True)

    # member_id = db.Column(db.Integer, db.ForeignKey("members.member_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    user = db.relationship("User", back_populates="event")

    # member = db.relationship("Member", back_populates="event")

    def __repr__(self):
        return f"<Event event_id={self.event_id} description={self.description}>"


#--------------------------------------------------------------------------------#

def connect_to_db(flask_app, db_uri="postgresql:///hfbc_church", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    db.create_all()