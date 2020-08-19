from flask_restful import Resource, reqparse
from models.user import User
from flask_jwt_extended import (
                                create_access_token,
                                create_refresh_token,
                                jwt_refresh_token_required,
                                get_jwt_identity,
                                jwt_required,
                                get_raw_jwt
                            )

_parse = reqparse.RequestParser()
_parse.add_argument('username', type=str, required=True, help="Enter your username")
_parse.add_argument('password', type=str, required=True, help="Enter your password")

from blacklist import BLACKLIST

class UserRegister(Resource):
    def post(self):

        data = _parse.parse_args()

        if User.get_user_by_name(data['username']):
            return {"message": "User already exsists"}, 400

        user = User(**data)
        user.save_into_db()

        return {"message": "User added successfully"}, 201


class UserLogin(Resource):
    def post(self):
        
        data = _parse.parse_args()
        
        user = User.get_user_by_name(data['username'])
        if user and user.password == data['password']:
            access_token = create_access_token(identity=user.id, fresh = True)
            refresh_token = create_refresh_token(user.id)
            
            return{
                "access_token": access_token,
                "refresh_token": refresh_token
            }, 201
            
        return {"message": "Wrong credentials"}, 400


class Refresh(Resource):
    
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        return {
            "new_access_token": new_token
        }
        
        
class UserLogout(Resource):
    
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        BLACKLIST.add(jti)
        return {"message": "You have successfully logged out"}