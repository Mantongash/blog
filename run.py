from flask import render_template
from app import app

# routes
@app.route("/")
def home():
  return render_template("index.html", title="Home")

#About route
@app.route("/about")
def about():
  return render_template("about.html", title="About")

if __name__ == "__main__":
  app.run(debug=True)