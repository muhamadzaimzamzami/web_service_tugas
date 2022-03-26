#Muhamad Zaim Zamzami (19090036) user : 19090036, pass:19090036
#Fatimatuzzahro (19090039) user 19090039, pass:19090039
import os
import random
import string

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import jsonify
import json
from flask_httpauth import HTTPTokenAuth
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.attributes import QueryableAttribute

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "user.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)
auth = HTTPTokenAuth(scheme='Bearer')

class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(80), unique=False, nullable=False, primary_key=False)
    token = db.Column(db.String(225), unique=True, nullable=True, primary_key=False)

#curl -i -X 
@app.route("api/v1/login", methods=["POST"])
def login():
    req = request.json;
    search = User.query.filter_by(username = req['username'], password = req['password']).first();
    if search:
        token = ''.join(random.choises(
            string.ascii_uppercase + string.digits, k=10
        ))

        User.query.filter_by(username = req['username'], password = req['password']).update({'token': token})
        db.session.commit()

        return {"token": token}, 200


@auth.verify_token
def verify_token(token):
  # ambil value token
  # cari ke dalam table user, 
  # return usernamenya

# tulis command line CURL utk request end point ini lengkap dengan data body jsonnya
@app.route("/api/v2/users/info", methods=["POST"])
@auth.login_required
def info()
  # response-kan {"username": auth.current_user()}, http code: 200