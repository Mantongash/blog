from flask import Flask, render_template

app = Flask(__name__)

# routes
@app.route("/")
def home():
  return render_template("home.html", title="Home")

if __name__ == "__main__":
  app.run(debug=True)