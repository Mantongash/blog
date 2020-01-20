from flask import render_template, request, logging, flash, url_for, redirect
from app import app
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt
from app.forms import SigninForm, SignupForm

app.config["SECRET_KEY"]="80fa202da9a998f467cd313ce4e64c04"

# Config MySQL
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "blog"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

# Initialize MYSQL
mysql = MySQL(app)

# routes
@app.route("/")
def home():
  return render_template("index.html", title="Home")

#About route
@app.route("/about")
def about():
  return render_template("about.html", title="About")

#Sign Up route
@app.route("/signup", methods=["POST", "GET"])
def signup():
  form = SignupForm(request.form)
  if request.method == "POST" and form.validate():
    username = form.username.data
    email= form.email.data
    password = sha256_crypt.encrypt(str(form.password.data))

    # Cursor
    cur = mysql.connection.cursor()

    cur.execute("INSERT INTO users(username,email, password) VALUES(%s,%s,%s)", (username, email, password))

        # Commit to DB
    mysql.connection.commit()

    # Close connection
    cur.close()

    flash("You have successfully registered and can now log in", "success")
    return redirect(url_for("signin"))

  return render_template("signup.html", title="Register", form=form)




#Sign In route
@app.route("/signin" methods=["POST", "GET"])
def signin():
  form = SignupForm()
  if form.validate_on_submit():
    return "</h1>" + form.username.data + " " + form.password.data + "</h1>"
  return render_template("signin.html", title="Sign In", form=form)

if __name__ == "__main__":
  app.run(debug=True)