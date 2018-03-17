#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask import request
from flask import Response, render_template

class Person(Resource):
  def get(self):
    return {
      # TODO: Not hard code this
      'person': [
        {
          'name': 'Oscar Andell',
          'title': 'IT student',
          'location':'Linköping, Sweden',
          'email':'Oscar@Andell.eu',
          'github':'https://github.com/OAndell/',
          'linkedin':'https://www.linkedin.com/in/oscar-andell-156ba0138/'
        }
      ]
    }
    
 
    

    

    
