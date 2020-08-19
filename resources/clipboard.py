from flask_restful import Resource, reqparse
from models.user import User, ClipboardModel
from flask_jwt_extended import (
                                create_access_token,
                                create_refresh_token,
                                jwt_refresh_token_required,
                                get_jwt_identity,
                                jwt_required,
                                get_raw_jwt
                            )

_parse = reqparse.RequestParser()
_parse.add_argument('sender_id', type=str, required=True, help="Sender ID required")
_parse.add_argument('sender', type=str, required=True, help="Sender NAME required")
_parse.add_argument('reciever_id', type=str, required=True, help="Reciever ID required")
_parse.add_argument('reciever', type=str, required=True, help="Reciever NAME required")
_parse.add_argument('time', type=str, required=True, help="Please provide the time of commit")
_parse.add_argument('content', type=str, required=True, help="Content value can not be empty")
_parse.add_argument('content', type=str, required=True, help="Content value can not be empty")
_parse.add_argument('checked', type=bool, required=True, help="Is the clip CHECKED?")

class Clipboard(Resource):
    def post(self):
        
        print("Hey i am the sender")
    
        data = _parse.parse_args()
        
        user = User.get_user_by_name(data['sender'])
        print(user)
        clip = ClipboardModel(**data, creator=user)
        clip.save_into_db()
        
        return {"message": "Clipboard added successfully"}, 201
        
        
class ClipboardSenderData(Resource):
    def get(self, user_id):
        
        user = User.get_user_by_id(user_id)
        if user is None:
            return {"message": "No user found with UID : {}".format(user_id)}
        
        clips = []
        return {"clips": [clip.json() for clip in ClipboardModel.get_clips_by_sender_id(user_id).all()]}, 201
    def delete(self, user_id):
        user = User.get_user_by_id(user_id)
        if user is None:
            return {"message": "No user found with UID : {}".format(user_id)}
        [clip.delete_from_db() for clip in ClipboardModel.get_clips_by_sender_id(user_id).all()]
        return {"message": "clip data deleted for user {}".format(user_id)}
        
        
class ClipboardSenderNData(Resource):
    
    def get(self, user_id, n):
        user = User.get_user_by_id(user_id)
        if user is None:
            return {"message": "No user found with UID : {}".format(user_id)}
        
        clips = []
        return {"clips": [clip.json() for clip in ClipboardModel.get_clips_by_sender_id(user_id).limit(n).all()]}, 201

 

class ClipboardRecieverData(Resource):
    def get(self, user_id):
        
        user = User.get_user_by_id(user_id)
        if user is None:
            return {"message": "No user found with UID : {}".format(user_id)}

        clips = []
        return {"clips": [clip.json() for clip in ClipboardModel.get_clips_by_reciever_id(user_id).all()]}, 201
        
class ClipboardRecieverNData(Resource):
    def get(self, user_id, n):
        
        user = User.get_user_by_id(user_id)
        if user is None:
            return {"message": "No user found with UID : {}".format(user_id)}
        clips = []
        return {"clips": [clip.json() for clip in ClipboardModel.get_clips_by_reciever_id(user_id).limit(n).all()]}, 201
    
    def put(self, user_id, n):
        
        user = User.get_user_by_id(user_id)
        if user is None:
            return {"message": "No user found with UID : {}".format(user_id)}
        elif n is not 1:
            return {"message": "Post can not be applied on bulk query"}
        else:
            
            clip = ClipboardModel.get_clips_by_reciever_id(user_id).first()
           
            clip.update_db()
            return {"clip": clip.json()}
        
        

