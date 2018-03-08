from flask_restful import Resource
from flask import request
from database.db import execute

class Frontpage(Resource):
  def get(self):
    base_url = request.host_url
    return {
        execute('SELECT * FROM test')
    }