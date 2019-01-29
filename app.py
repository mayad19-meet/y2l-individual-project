from flask import Flask
from flask import Flask,render_template,url_for,request, redirect
import database


app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for("log_in"))

@app.route('/log_in', methods=["GET", "POST"])
def log_in():
    if request.method == "GET":
        return render_template("login.html")
    else:
        return redirect(url_for("home"))

@app.route('/home')
def home():
    return render_template("personalproj-cs-home.html")

@app.route('/grammar')
def grammar():
    return render_template("grammar.html")

@app.route('/sentences')
def sentences():
    return render_template("sentences.html")
@app.route('/quiz')
def quiz():
    return render_template("practice.html")

@app.route('/videos')
def videos():
    return render_template("videos.html") 

#@app.route('/log_in', methods=["GET", "POST"])
#def log_in():
 #   if request.method == "GET":
  #      return render_template("login.html")
   # else:
    #    pass


@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")  
    else:
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        username = request.form["username"]
        password = request.form["password"]

        database.add_account(first_name,last_name,username,password)

        return "You have signed up!! Now go back and click the log in button!"


if __name__ == '__main__':
    app.run(debug=True)

