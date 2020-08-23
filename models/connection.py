from flask_restful import Resource, reqparse
from sqlalchemy import desc
from models.pc_user import UserModel
from db import db

class ConnectionModel(db.Model):
    __tablename__ = "connections"
    
    id = db.Column(db.Integer, primary_key=True)
    id_sender = db.Column(db.Integer, nullable=False)
    id_reciever = db.Column(db.Integer, nullable=False)
    
    @classmethod
    def get_id_by_uuid(cls, uuid):
        return UserModel.get_id_by_uuid(uuid)
    
    @classmethod
    def get_connections_by_id(cls, _id):
        return cls.query.filter_by(id_sender=_id)
    
    def save_to_database(self):
        db.session.add(self)
        db.session.commit()

    