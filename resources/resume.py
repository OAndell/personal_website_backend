from flask_restful import Resource, reqparse
from flask import request
from flask import Response, render_template
from database.db import execute


parser = reqparse.RequestParser()
parser.add_argument('id', type=str, required=True)

class Resume(Resource):

  #get all entries
  def get(self):
      return execute('SELECT * FROM resume')

  #get entries for a specific user
  def post(self):
     args = parser.parse_args()
     return execute('SELECT *  FROM resume WHERE personID = %s ORDER BY id', args['id'])

