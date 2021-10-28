from flask import Flask
app = Flask(__name__)

@app.route("/")
def welcome():
    return f"Hello World!"

@app.route("/dojo")
def dojo_page():
    return f"Dojo!"

@app.route("/say/<string:username>")
def user_page(username):
    print(username)
    return f"Hi: " + username

@app.route("/repeat/<int:number>/<string:random>")
def repeat_page(number, random):
    return number * random

if __name__=="__main__":
    app.run(debug=True)