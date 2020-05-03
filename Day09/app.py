from flask import Flask, render_template
app = Flask(__name__)

# @app.route("/ak")
# def hi():
#     return "Hello World"

# @app.route("/tanish")
# def hii():
#     return "Hello Tanish"

# @app.route("/superman")
# def superman():
#     return "The man of steel"

# @app.route("/<name>")
# def hello(name):
#     return "<h1> Hello </h1>" + name

@app.route("/home")
def homePage():
    return render_template("home.html")

@app.route("/")
def htmlPage():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True,port=8000)