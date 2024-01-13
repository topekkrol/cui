from flask import Flask, request, abort

app = Flask(__name__)

# import declared routes
import test
@app.route("/")
def index():
    return ("index.html")

@app.route("/John")
def John(imie='Test'):
    return "Hello " + imie + "!"


if __name__ == "__main__":
    app.run(debug=True)