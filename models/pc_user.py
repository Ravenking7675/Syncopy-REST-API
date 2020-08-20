from flask_restful import Resource, reqparse
from sqlalchemy import desc
from db import db


class UserModel(db.Model):
    __tablename__="userdata"
    
    id = db.Column(db.Integer,
        primary_key=True)
    
    username = db.Column(db.String, nullable=False, unique=True)
    uuid = db.Column(db.Unicode, nullable=False, unique=True)
    isPc = db.Column(db.Boolean)
    
    def save_into_db(self):
        
        db.session.add(self)
        db.session.commit()    