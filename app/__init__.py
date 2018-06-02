from flask import Flask

app = Flask(__name__)
app.config.from_pyfile("../config.cfg")
CONFIG = app.config

from app import views