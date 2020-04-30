from flask import Flask
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

@app.route("/<name>")
def hello(name):
    return "Hello " + name


if __name__ == "__main__":
    app.run(debug=True,port=8000)