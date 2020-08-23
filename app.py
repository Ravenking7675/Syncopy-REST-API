from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

from resources.encrypt import Encrypt, GetUUID
from resources.connection import Connection, FindConnections

from resources.clipboard import (Clipboard, 
                                 ClipboardSenderData, 
                                 ClipboardRecieverData, 
                                 ClipboardRecieverNData,
                                 ClipboardSenderNData)

from resources.user import UserRegister, UserLogin, Refresh,UserLogout
from flask_jwt_extended import JWTManager
from db import db
from blacklist import BLACKLIST
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.secret_key = "notice me senpai"
api = Api(app)

jwt = JWTManager(app)

api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, "/auth")
api.add_resource(Refresh, "/refresh")
api.add_resource(UserLogout, "/logout")
api.add_resource(Clipboard, "/clip") #<string:name>
api.add_resource(ClipboardSenderData, "/sent/<string:user_uuid>")
api.add_resource(ClipboardSenderNData, "/sent/<string:user_uuid>/<int:n>")
api.add_resource(ClipboardRecieverData, "/recieved/<string:user_uuid>")
api.add_resource(ClipboardRecieverNData, "/recieved/<string:user_uuid>/<int:n>")
api.add_resource(Encrypt, "/generate_key")
api.add_resource(GetUUID, "/key/<string:name>")
api.add_resource(Connection, "/add_connection")
api.add_resource(FindConnections, "/connections/<string:uuid>")

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    print("checking jti token")
    return decrypted_token['jti'] in BLACKLIST

@jwt.revoked_token_loader
def revoked_token_callback():
    return jsonify({"message": "You are currently not logged in"})
 
if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)