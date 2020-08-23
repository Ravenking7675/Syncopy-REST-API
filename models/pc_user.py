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
        
    @classmethod
    def get_user_by_uuid(cls, uuid_):
        return cls.query.filter_by(uuid=uuid_).first()
    
    @classmethod
    def get_user_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()    
    
    @classmethod
    def get_uuid_by_name(cls, name):
        return cls.query.filter_by(username=name).first()
        
    @classmethod
    def get_id_by_uuid(cls, uuid):
        return cls.query.filter_by(uuid=uuid).first() 
    
    def json(self):
        return {"username": self.username, "uuid": self.uuid, "isPc": self.isPc}