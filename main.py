from flask import Flask, render_template, request
from database import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'changeme'

# TODO: Add all of the routes you want below this line!


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/north")
def north():
    return render_template("north.html")


@app.route("/south")
def south():
    return render_template("south.html")


@app.route("/center")
def center():
    return render_template("center.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

    
@app.route("/ask", methods = ['GET', 'POST'])
def ask():
  if request.method == 'GET':
    return render_template('contact.html')
  else:
    username = request.form['fullname']
    text = request.form['question'] 
    add_question(username, text)
    return render_template('contact.html')


  




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
