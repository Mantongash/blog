from flask import render_template
from app import app

# routes
@app.route("/")
def home():
  return render_template("index.html", title="Home")

if __name__ == "__main__":
  app.run(debug=True)