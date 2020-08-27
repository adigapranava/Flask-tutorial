from flask import Flask, render_template,request, url_for, redirect, session, flash
import bcrypt
from datetime import timedelta
import sql_db

def encrpt(password):
   passwd = password.encode()
   salt = bcrypt.gensalt()
   hashed = bcrypt.hashpw(passwd, salt)
   return hashed
   

app = Flask(__name__)
app.secret_key = 'random string'
app.permanent_session_lifetime = timedelta(minutes = 5) #save section for x mins/hours

@app.route('/')
@app.route('/home')
def index():
   return render_template('index.html')

@app.route("/register", methods = ['GET', 'POST'])
def register():
   #error = None
   
   if request.method == 'POST':
      #session.permanent = True
      email = request.form['email']
      password = encrpt(request.form['password'])#generate_password_hash(request.form['password'])
      age = request.form['age']
      msg = sql_db.enter_to_db(email, password, age)
      if msg[0]:
         flash(msg[1])
         session["email"] = email
         return redirect(url_for('index'))
      else:
         flash(msg[1])
         return redirect(url_for('login'))
      #return render_template('login.html', error = error)
   else:
      if "email" in session:
         flash("You have been already logged in!")
         return redirect(url_for("index"))
      else:
         return render_template("register.html")
   

@app.route('/login', methods = ['GET', 'POST'])
def login():
   error = None
   
   if request.method == 'POST':
      session.permanent = True
      email = request.form['email']
      password = request.form['password'] #generate_password_hash(request.form['password'])
      msg = sql_db.check_if_exist(email, password)
      if msg[0]:         
         session["email"] = email
         flash(msg[1])
         return redirect(url_for('index'))
      else:
         error = msg[1]
         return render_template('login2.html', error = error)
      flash('You were successfully logged in')
      return redirect(url_for('index'))
		#return render_template('login.html', error = error)
   else:
      if "email" in session:
         flash("You have been already logged in!")
         return redirect(url_for("index"))
      else:
         return render_template("login2.html")

@app.route("/logout")
def logout():
   if "email" in session:
      flash("You have been logged out!!", "info")
      session.pop("email", None)
   else:
      flash("You have not logged in!!", "info")
   return redirect(url_for("login"))

@app.route("/team")
def team():
   return render_template('team.html')



if __name__ == "__main__":
   sql_db.create_db()
   print("hai")
   app.run(debug = True)
   print(3)