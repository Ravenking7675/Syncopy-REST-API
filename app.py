from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from resources.user import UserRegister, UserLogin, Refresh,UserLogout
from flask_jwt_extended import JWTManager
from db import db
from blacklist import BLACKLIST

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
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

@app.before_first_request
def create_tables():
    db.create_all()
    
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