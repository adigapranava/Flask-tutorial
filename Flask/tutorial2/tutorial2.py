from flask import Flask,render_template,redirect,url_for

app = Flask(__name__)


@app.route("/<name>")
def home(name):
	return render_template("home.html", content=name, names = ["mani", "ravi","kavi","hari"]) # sending name to the frontend


if __name__ == "__main__":
	app.run()