from flask_restful import Resource
from flask import request
from flask import Response, render_template

class Frontpage(Resource):
  def get(self):
    return Response(render_template('frontpage.html'),mimetype='text/html')
    
