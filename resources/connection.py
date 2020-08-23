from flask_restful import Resource, reqparse
from models.connection import ConnectionModel
from models.pc_user import UserModel
from flask_jwt_extended import (
                                create_access_token,
                                create_refresh_token,
                                jwt_refresh_token_required,
                                get_jwt_identity,
                                jwt_required,
                                get_raw_jwt
                            )


_parse = reqparse.RequestParser()
_parse.add_argument('uuid_sender', type=str, required=True, help="Please pass sender's UUID")
_parse.add_argument('uuid_reciever', type=str, required=True, help="Please pass reciever's UUID")

class Connection(Resource):
    def post(self):
        data = _parse.parse_args()
        
        id_sender = UserModel.get_id_by_uuid(data['uuid_sender']).id
        id_reciever = UserModel.get_id_by_uuid(data['uuid_reciever']).id
        
        if id_sender == id_reciever:
            return {"message": "UUIDs can not be same", "response": 400}, 400
        
        if id_sender is None or id_reciever is None:
            return {"message": "Check the UUIDs once again", "response": 400}, 400
        
        sender = ConnectionModel.get_id_by_uuid(data['uuid_sender'])
        
        reciever_id = sender.id_reciever
        
        if id_reciever == reciever_id:
            return {"message": "Connection already present", "response": 400}, 400
        
        connection = ConnectionModel(id_sender=id_sender, id_reciever=id_reciever)
        connection.save_to_database()
        
        connection = ConnectionModel(id_sender=id_reciever, id_reciever=id_sender)
        connection.save_to_database()
        
        return{"message": "connection established", "response": 201}, 201


class FindConnections(Resource):
    def get(self, uuid):
        
        uid = ConnectionModel.get_id_by_uuid(uuid)
        if uid is None:
            return {"connections": [], "response": 404}, 404
        
        users = ConnectionModel.get_connections_by_id(uid.id)
        connections = []
        
        for user in users:
            id = user.id_reciever
            print(id)
            connections.append(UserModel.get_user_by_id(id).json())
        
        return {"connections": connections, "response": 201}, 201