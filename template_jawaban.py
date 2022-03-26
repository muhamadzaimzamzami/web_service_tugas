
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


