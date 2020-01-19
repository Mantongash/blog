from flask import render_template
from app import app
from app.forms import SigninForm, SignupForm

app.config["SECRET_KEY"]="80fa202da9a998f467cd313ce4e64c04"

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
  form = SignupForm()
  return render_template("signup.html", title="Register", form=form)

#Sign In route
@app.route("/signin")
def signin():
  form = SignupForm()
  return render_template("signin.html", title="Sign In", form=form)

if __name__ == "__main__":
  app.run(debug=True)