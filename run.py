from flask import render_template
from app import app
from app.forms import SigninForm, SignupForm

# routes
@app.route("/")
def home():
  return render_template("index.html", title="Home")

#About route
@app.route("/about")
def about():
  return render_template("about.html", title="About")

#Sign Up route
@app.route("/signup")
def signup():
  return render_template("signup.html", title="Register")

#Sign In route
@app.route("/signin")
def signin():
  return render_template("signin.html", title="Sign In")

if __name__ == "__main__":
  app.run(debug=True)