from flask_restful import Resource, reqparse
from flask import request
from flask import Response, render_template
from database.db import execute

parser = reqparse.RequestParser()
parser.add_argument('personID', type=str, required=True)

class Theme(Resource):

  #get all entries
  def get(self):
      return execute('SELECT * FROM colortheme')

  #get entries for a specific user
  def post(self):
    try:
       args = parser.parse_args()
       return execute('SELECT * FROM colortheme WHERE personID = %s',args['personID'])
    except Exception as e:
           return {'error': str(e)}
