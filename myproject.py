from flask import Flask
from flask_restful import Api
from resources.frontpage import Frontpage
from resources.person import Person
app = Flask(__name__)

#Init the framework that i am using for the REST API
api = Api(app)
api.add_resource(Frontpage, '/')

api = Api(app)
api.add_resource(Person, '/person')


@app.route("/info")
def main():
    return "<h1 style='color:green'>Hosted in my room</h1>"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
