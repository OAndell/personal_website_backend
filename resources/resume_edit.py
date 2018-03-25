from flask_restful import Resource, reqparse
from flask import request
from flask import Response, render_template
from database.db import execute
import hashlib, uuid
import json

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True)
parser.add_argument('password', type=str, required=True)
parser.add_argument('newdata', type=str, required=True)


class Resume_edit(Resource):
  
  def post(self):
    try:
       args = parser.parse_args()
       username=args['username']
       password=args['password']
       salt = uuid.uuid4().hex
       user = execute('SELECT *  FROM user WHERE username = %s', username)
       if(user[0]['password'] == hashlib.sha512(password.encode()+ user[0]['salt'].encode()).hexdigest()):
            newdataJson = json.loads(args['newdata'].replace("'",'"'))
            execute('''
              UPDATE resume SET 
              title=%s, body=%s
              WHERE personID=%s AND displayorder=%s''',
              (
                newdataJson['title'], newdataJson['body'],
                newdataJson['personID'], newdataJson['displayorder']
            ))
            return {'success': True}
       else:
           return {'success': False}
    except Exception as e:
           return {'error': str(e)}
