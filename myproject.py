from flask import Flask
from flask_restful import Api
from resources.frontpage import Frontpage
from resources.resume import Resume
from resources.person import Person
from resources.auth import Auth
from resources.person_edit import Person_edit
from resources.resume_edit import Resume_edit
from resources.resume_add import Resume_add


app = Flask(__name__)

api = Api(app)
api.add_resource(Frontpage, '/')

api = Api(app)
api.add_resource(Person, '/person')
api.add_resource(Resume, '/resume')
api.add_resource(Auth, '/auth')
api.add_resource(Person_edit, '/person_edit')
api.add_resource(Resume_edit, '/resume_edit')
api.add_resource(Resume_add, '/resume_add')

@app.route("/info")
def main():
    return "<h1 style='color:green'>Hosted in my room</h1>"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
