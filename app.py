from flask import Flask
from flask import Flask,render_template,url_for,request
app = Flask(__name__)

@app.route('/')
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

@app.route('/log_in')
def log_in():
    return render_template("login.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")           
if __name__ == '__main__':
    app.run(debug=True)

