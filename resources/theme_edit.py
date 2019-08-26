from flask_restful import Resource, reqparse
from flask import request
from flask import Response, render_template
from database.db import execute
import hashlib, uuid
import json

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True)
parser.add_argument('password', type=str, required=True)
parser.add_argument('theme', type=str, required=True)


class Theme_edit(Resource):
  
  def post(self):
    try:
       args = parser.parse_args()
       username=args['username']
       password=args['password']
       salt = uuid.uuid4().hex
       user = execute('SELECT *  FROM user WHERE username = %s', username)
       if(user[0]['password'] == hashlib.sha512(password.encode()+ user[0]['salt'].encode()).hexdigest()):
            newdataJson = json.loads(args['theme'].replace("'",'"'))
            execute('''
              INSERT INTO colortheme
              (personID, main, background, background_lines, textcolor, textcolor2)
              VALUES(%s, %s, %s, %s, %s, %s)
              ON DUPLICATE KEY UPDATE
              main = %s, background=%s, background_lines=%s,
              textcolor=%s, textcolor2=%s
              ''',
              (
                newdataJson['personID'], newdataJson['main'],
                newdataJson['background'], newdataJson['background_lines'],
                newdataJson['textcolor'], newdataJson['textcolor2'],
                newdataJson['main'],newdataJson['background'],
                newdataJson['background_lines'], newdataJson['textcolor'],
                newdataJson['textcolor2']
            ))
            
            return {'success': True}
       else:
           return {'success': False}
    except Exception as e:
           return {'error': str(e)}
