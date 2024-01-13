from flask import Flask, render_template, redirect, request, url_for
import random
app = Flask(__name__, template_folder="templates")
imie = "test"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/handle_input", methods=["POST"])
def handle_input():
    choice = request.form.get("choice")
    if choice == "1":
        return redirect(url_for("John"))
    elif choice == "2":
        return redirect(url_for("welcome_number"))
    else:
        return "Incorrect value, please try again."

@app.route("/John")
def John():
    return "Hello " + imie + "!"

@app.route("/Welcome/number", methods=["GET", "POST"])
def welcome_number():
    if request.method == "POST":
        return redirect(url_for("dodatkowy_przycisk"))

    liczba = random.randint(1,5)
    return render_template("welcome_number.html", liczba=liczba)

@app.route("/dodatkowy_przycisk", methods=["GET", "POST"])
def dodatkowy_przycisk():
    if request.method == "POST":
        choice = request.form.get("choice")
        print(f"43 Received choice: {choice}")
        if choice == "3":
            return redirect(url_for("index"))
        else:
            return f"Welcome with choice: {choice}"#
    else:
        return "Method Not Allowed"

if __name__ == "__main__":
    app.run(debug=True)