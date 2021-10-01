from flask import Flask, request

from factorial import factorial

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<name>")
def hello_utkarsh(name):
    return "<p>Hello, {}!</p>".format(name)

@app.route("/factorial/<value>")
def fac(value):
    res=factorial(int(value))
    return "<p>Hello, {}!</p>".format(res)

if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()