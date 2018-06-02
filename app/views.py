from flask import render_template
from app import app
from app import controller as controller
from app import feed



@app.route('/')
def index():
	controller.load_client()
	return render_template('index.html')

