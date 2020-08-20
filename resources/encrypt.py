from uuid import getnode as get_mac
from math import floor, ceil
from random import randint
from flask_restful import Resource, reqparse


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
            return {"UUID": key}
        
        else:
            
            userid = unique_str
            limit = len(userid)-2
            
            A = userid[randint(0,limit)]
            B = userid[randint(0,limit)]
            C = userid[randint(0,limit)]
            D = userid[randint(0,limit)]
            E = userid[randint(0,limit)]
            F = userid[randint(0,limit)]
            
            key = A+C+E+B+D+F
            return {"UUID": key}
            
                
            
            