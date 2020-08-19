from flask_restful import Resource, reqparse
from sqlalchemy import desc
from db import db

class ClipboardModel(db.Model):
    
    __tablename__="clipboard"
    
    id = db.Column(db.Integer,primary_key=True)
    sender = db.Column(db.String(80))
    sender_id = db.Column(db.Integer)
    reciever = db.Column(db.String(80))
    reciever_id = db.Column(db.Integer)    
    time = db.Column(db.Integer)
    content = db.Column(db.UnicodeText)
    checked = db.Column(db.Boolean, default=False)
    user_id = db.Column('user_id', db.ForeignKey("user.id"))
   
    @classmethod
    def get_clip_by_sender_name(cls, name):
        return cls.query.filter_by(sender=name).all()
    
    @classmethod
    def get_clip_by_reciver_name(cls, name):
        return cls.query.filter_by(reciever=name).all()
    
    @classmethod
    def get_clip_by_sender_id(cls, _id):
        return cls.query.filter_by(id=_id).all()

    def save_into_db(self):
        db.session.add(self)
        db.session.commit()
    
    def update_db(self):
        self.checked = True
        db.session.flush()
        db.session.commit()
    
    @classmethod
    def get_clips_by_sender_id(cls, user_id):
        return cls.query.order_by(desc(ClipboardModel.time)).filter_by(sender_id=user_id)
    
    @classmethod
    def get_clips_by_reciever_id(cls, user_id):
        return cls.query.order_by(desc(ClipboardModel.time)).filter_by(reciever_id=user_id)
    
    def json(self):
        return {
                "sender": self.sender,
                "reciever": self.reciever,
                "sender_id": self.sender_id,
                "reciever_id": self.reciever_id,
                "time": self.time,
                "checked": self.checked,
                "content": self.content
                }
        
    
    
class User(db.Model):
    
    __tablename__="user"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    master = db.relationship("ClipboardModel", backref = 'creator', lazy='dynamic')
    
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