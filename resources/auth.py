from flask_restful import Resource, reqparse
from flask import request
from flask import Response, render_template
from database.db import execute
import hashlib, uuid

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True)
parser.add_argument('password', type=str, required=True)
class Auth(Resource):
  
  def post(self):
       args = parser.parse_args()
       username=args['username']
       password=args['password']
       salt = uuid.uuid4().hex
       user = execute('SELECT *  FROM user WHERE username = %s', username)
       if(user[0]['password'] == hashlib.sha512(password.encode()+ user[0]['salt'].encode()).hexdigest()):
            return {'success': True, 'token': None}
       else:
           return {'success': False, 'token': None}
          
  def get(self):
        return execute('SELECT *  FROM user')
  
