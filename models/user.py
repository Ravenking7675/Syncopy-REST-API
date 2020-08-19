from flask_restful import Resource, reqparse
from db import db

class UserModel(db.Model):
    
    __tablename__="users"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False, unique=True)
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    @classmethod
    def get_user_by_name(cls, username):
        print("Hey i am from user model")
        return cls.query.filter_by(username = username).first()

    @classmethod
    def get_user_by_id(cls, _id):
        print("Hey i am from user model")
        return cls.query.filter_by(id = _id).first()

    def save_into_db(self):
        db.session.add(self)
        db.session.commit()

    