from flask import Flask, render_template
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, PasswordField, validators
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap


app = Flask(__name__)


class SignupForm(FlaskForm):
    email = StringField(label='Email: ', validators=[DataRequired(), Email(message="It requires '@' or '.'")])
    password = PasswordField(label='Password: ', validators=[DataRequired(), validators.Length(min=8)])
    button = SubmitField(label='Log In')




@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = SignupForm(meta={'csrf': False})
    form.validate_on_submit()
    if form.validate_on_submit():
        if form.email.data == 'admin@email.com' and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form_=form)


if __name__ == '__main__':
    Bootstrap(app)
    app.run(debug=True)