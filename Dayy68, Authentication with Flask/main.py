import flask
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)




app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        name_ = request.form["name"]
        pass_ = generate_password_hash(password=request.form['password'], method='pbkdf2:sha256', salt_length=8)
        new_user = User(email=request.form["email"], password=pass_, name=name_)
        db.session.add(new_user)
        db.session.commit()
        return render_template("secrets.html", name_tag=name_)
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form["email"]).first()
        if user:
            if check_password_hash(user.password, request.form["password"]):
                flash("Login successfully!")
                login_user(user)
                #logout_user(user) -> to log out
                return redirect(url_for('secrets', name=user.name))
            else:
                flash("Wrong e-mail or password. Please try again.")
        else:
            flask.flash("That user does not exist. ")
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    name_ = request.args.get("name")
    return render_template("secrets.html", name_tag=name_, logged_in=True)


@app.route('/logout')
def logout():
    pass


@app.route('/download')
def download():
    return send_from_directory(directory="static", path="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
