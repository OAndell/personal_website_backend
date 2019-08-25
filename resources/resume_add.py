from flask_restful import Resource, reqparse
from flask import request
from flask import Response, render_template
from database.db import execute
import hashlib, uuid
import json

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True)
parser.add_argument('password', type=str, required=True)
parser.add_argument('personID', type=str, required=True)


class Resume_add(Resource):
  
  def post(self):
    try:
       args = parser.parse_args()
       username=args['username']
       password=args['password']
       personID=args['personID']
       salt = uuid.uuid4().hex
       user = execute('SELECT *  FROM user WHERE username = %s', username)
       if(user[0]['password'] == hashlib.sha512(password.encode()+ user[0]['salt'].encode()).hexdigest()):
            execute('''
                INSERT INTO resume (personID, title, body) 
                VALUES (%s, %s, %s)''',
                (
                    personID, "<h2>New Title</h2>", "New Body"
                )
            )
            return {'success': True}
       else:
           return {'success': False}
    except Exception as e:
           return {'error': str(e)}
