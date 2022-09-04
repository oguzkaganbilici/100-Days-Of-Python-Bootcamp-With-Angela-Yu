from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import Label, IntegerField,SubmitField
from wtforms.validators import DataRequired
from markupsafe import escape

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(app)


class books(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(250), unique=True, nullable=False)
    author = db.Column("author", db.String(250), nullable=False)
    rating = db.Column("rating", db.Float, nullable=False)

    def __init__(self, title, author, rating):
        self.title = title
        self.author = author
        self.rating = rating


class EditPage(FlaskForm):
    book_title = Label(field_id=0,text="Book's Title:")
    current_rating = Label(field_id=1, text="Current Rating")
    new_rating = IntegerField('', validators=[DataRequired()])
    submit = SubmitField('Change Rating')


@app.route('/')
def home():
    all_books = db.session.query(books).all()
    return render_template('index.html', books=all_books)



@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_book = books(request.form['book_name'], request.form['author_name'], request.form['rating'])
        db.session.add(new_book)
        db.session.commit()

    return render_template('add.html')


@app.route('/edit/<book_id>', methods=['GET', 'POST'])
def edit(book_id):
    if request.method == 'GET':
        _id = book_id
        _title = db.session.query(books).get(book_id).title
        _rating = db.session.query(books).get(book_id).rating
        return render_template('edit.html',  title_=_title, rating_=_rating, id_=_id)

    elif request.method == 'POST':
        new_ranking = request.form["new_rating"]
        id = request.form["_id_"]
        ranking_update = books.query.filter_by(id=escape(id)).first()
        ranking_update.rating = new_ranking
        db.session.commit()
        """
        ranking_update = books.query.filter_by(id=books_id).first()
        ranking_update.rating = new_ranking
        db.session.commit()
        """
        return redirect(url_for('home'))


@app.route("/delete")
def delete_book():
    _id = request.args.get('delete_id')
    delete_ = books.query.filter_by(id=_id).delete()
    db.session.commit()
    return redirect(url_for('home'))



if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

