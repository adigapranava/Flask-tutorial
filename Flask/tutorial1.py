#getting started wit Flask

from flask import Flask, redirect, url_for

app = Flask(__name__)

a =False

@app.route("/")
def home():
	return "Hello! this is main page <h1>haii</h1"

@app.route("/<name>")
def user(name):
	global a
	if a is False:
		a = True
	else:
		a = False
	return f"<h1>Hello {name}</h1>"
	

@app.route("/admin/")
def admin():
	if a is False:
		return redirect(url_for("home")) #if a is False u cannot visit admins page
	else:
		return redirect(url_for("user",name = "Admin!")) #"<h1>You are in admin page</h1><br"

if __name__ == "__main__":
	app.run()
