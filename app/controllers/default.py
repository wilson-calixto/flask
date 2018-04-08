from app import app
from flask import render_template

#add um valor default a uma var

#pegando uma variavel pela url tipo get
@app.route("/test/<name>",defaults={'name':None})
@app.route("/test/<name>")
def test(name):
	if name:
		return "ola,%s" % name
	else:
		return  "ola, user" 

#vc pode pegar um numero tambem

@app.route("/numero/<int:num>")
def numero(num):
	if num:
		return "ola,%d" % num
	else:
		return  "numnum" 		


		
@app.route("/index/",defaults={'user':None})
@app.route("/index/<user>")
def index(user):
	return  render_template('index.html',
		user=user
		) 
