import os
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql6496825:kqueNJcK9M@sql6.freemysqlhosting.net/sql6496825'


from Api import models
from Api import views
