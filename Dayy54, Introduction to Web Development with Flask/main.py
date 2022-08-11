from flask import Flask
from random import randint

app = Flask(__name__)


def make_bold(func):
    def wrapper():
        return f"<h1> {func()}</h1>"
    return wrapper


@app.route("/")
@make_bold
def main():
    return "Guess a number between 0 and 9:" \
           "<br> </br>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

rand_number = randint(1, 10)


@make_bold
@app.route("/<int:user_select>")
def go_answer(user_select):
    if int(user_select) < rand_number:
        return "<h1 style='color:Red;'>Too low, try again </h1>" \
               "<br></br>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"\

    elif int(user_select) > rand_number:
        return "<h1 style='color:Purple;'>Too High, try again </h1>" \
               "<br></br>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"\

    else:
        return "<h1 style='color:green;'>You found me </h1>" \
               "<br></br>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"\


if __name__ == "__main__":
    app.run(debug=True)