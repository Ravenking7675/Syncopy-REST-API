from uuid import getnode as get_mac
from math import floor, ceil
from models.pc_user import UserModel
from random import randint
from flask_restful import Resource, reqparse
from sqlalchemy.exc import IntegrityError


_parse = reqparse.RequestParser()
_parse.add_argument('unique_str', type=str, required=True, help="Please pass the unique string")
_parse.add_argument('username', type=str, required=True, help="Please give the username")
_parse.add_argument('isPc', type=bool, required=True, help="Is the request comming from a PC?")

class Encrypt(Resource):

    def post(self):
        
        data = _parse.parse_args()
        unique_str = data['unique_str']

        if data['isPc']:
            
            mac = unique_str
            username = data['username']

            A = mac[randint(0,14)]
            B = mac[randint(0,14)]
            C = mac[randint(0,14)]

            e1 = int(mac[randint(0,14)])
            e2 = int(mac[randint(0,14)])
            e3 = int(mac[randint(0,14)])

            D = username[floor(e1/2)]
            E = username[ceil(e2/2)]
            F = username[floor(e3/2)]
            
            key = A+C+E+B+D+F
            
            try:
                user = UserModel(username=username, uuid=key, isPc = False)
                user.save_into_db()
                return {"UUID": key}, 201
            except IntegrityError as e:
                return {"message": "Username already exists"}, 400
        
        else:
            
            userid = unique_str
            limit = len(userid)-2
            username = data['username']

            A = userid[randint(0,limit)]
            B = userid[randint(0,limit)]
            C = userid[randint(0,limit)]
            D = userid[randint(0,limit)]
            E = userid[randint(0,limit)]
            F = userid[randint(0,limit)]
            
            key = A+C+E+B+D+F
            
            try:
                user = UserModel(username=username, uuid=key, isPc = False)
                user.save_into_db()
                return {"UUID": key}, 201
            except IntegrityError as e:
                return {"message": "Username already exists"}, 400
            
                
class GetUUID(Resource):
    def get(self, name):
        
        user = UserModel.get_uuid_by_name(name)
        if user is None:
            return {"message": "no user exist with Username : {}".format(name)}, 404
        return {"uuid": user.uuid}, 201