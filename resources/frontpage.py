from flask_restful import Resource
from flask import request
from database.db import execute
from flask import Response, render_template

class Frontpage(Resource):
  def get(self):
    base_url = request.host_url
    return Response(render_template('frontpage.html'),mimetype='text/html')
    
