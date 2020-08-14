#passing elements to front end 


from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
c =1

a =False

@app.route("/<name>")
def home(name):
	global c
	c += 1
	return render_template("home.html",content=name, r=c) # sending name to the frontend


if __name__ == "__main__":
	app.run()
