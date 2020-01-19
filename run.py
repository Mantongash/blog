from flask import Flask, render_template
from app import app

app = Flask(__name__)

# routes
@app.route("/")
def home():
  return render_template("index.html", title="Home")

if __name__ == "__main__":
  app.run(debug=True)