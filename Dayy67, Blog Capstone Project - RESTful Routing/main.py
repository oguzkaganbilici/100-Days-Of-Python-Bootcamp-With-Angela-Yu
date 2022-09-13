from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime

## Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    #body = StringField("Blog Content", validators=[DataRequired()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    posts = db.session.query(BlogPost).all()
    requested_post = None
    for blog_post in posts:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/new-post", methods=["GET", "POST"])
def new_post():
    header = "New Post"
    form = CreatePostForm()
    full_date = datetime.now()
    month = full_date.strftime("%B")
    day = full_date.strftime("%d")
    year = full_date.strftime("%Y")
    full_date_ = month+" "+day+","+year
    if form.validate_on_submit():
        new_post_ = BlogPost(title=form.title.data, subtitle=form.subtitle.data, date=full_date_, body=form.body.data,
                             author=form.author.data, img_url=form.img_url.data)

        db.session.add(new_post_)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template('make-post.html', form_=form, header_=header)


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    header = "Edit Post"
    post__ = db.session.query(BlogPost).filter_by(id=post_id).first()
    form = CreatePostForm(title=post__.title, subtitle=post__.subtitle, author=post__.author, img_url=post__.img_url,
                          body=post__.body)
    if form.validate_on_submit():
        post__.title = form.title.data
        post__.subtitle = form.subtitle.data
        post__.author = form.author.data
        post__.img_url = form.img_url.data
        post__.body = form.body.data
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form_=form, header_=header)

@app.route("/delete/<int:post_id>")
def delete(post_id):
    db.session.query(BlogPost).filter_by(id=post_id).delete()
    db.session.commit()
    return redirect(url_for("get_all_posts"))


if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)