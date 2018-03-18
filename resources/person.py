
from flask_restful import Resource, reqparse
from flask import request
from flask import Response, render_template
from database.db import execute


parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)

class Person(Resource):

  #get all users
  def get(self):
      return execute('SELECT * FROM person')

  #get specific user
  def post(self):
     args = parser.parse_args()
     return execute('SELECT * FROM person WHERE name = %s', args['name'])

  
    
 
    

    

    
