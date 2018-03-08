from flask import Flask
from flask_restful import Api

from resources.frontpage import Frontpage

app = Flask(__name__)

# Init the framework that i am using for the REST API
api = Api(app)


api.add_resource(Frontpage, '/')


if __name__ == '__main__':
    app.run()
