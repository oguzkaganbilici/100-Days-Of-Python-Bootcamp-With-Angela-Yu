from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

API_KEY = "2e1716b76f9462b12317814b176ce175"

URL_ = "https://api.themoviedb.org/3/search/movie?"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///My-Top-10-Movies.db"


class Movie(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(20), nullable=False)
    year = db.Column("year", db.Integer)
    description = db.Column("description", db.String(500))
    rating = db.Column("rating", db.Integer)
    ranking = db.Column("ranking", db.Integer)
    review = db.Column("review", db.String(250))
    img_url = db.Column("img_url", db.String(50))

    def __int__(self, title, year, description, rating, ranking, review, img_url):
        self.title = title
        self.year = year
        self.description = description
        self.rating = rating
        self.ranking = ranking
        self.review = review
        self.img_url = img_url


class QuickFormEdit(FlaskForm):
    new_rating = StringField(label="Your rating out of 10 e.g:7.5", validators=[DataRequired()])
    new_review = StringField(label="Your review", validators=[DataRequired()])
    submit_button = SubmitField(label="Done")


class QuickFormAdd(FlaskForm):
    new_title = StringField(label="Movie Title", validators=[DataRequired()])
    add_button = SubmitField(label="Add Movie")


@app.route("/")
def home():
    #all_movies = db.session.query(Movie).all()
    all_movies = Movie.query.order_by(Movie.rating).all()
    movies = []
    for movie in all_movies:
        movies.append({"id": movie.id, "title": movie.title, "year": movie.year, "description": movie.description,
                       "rating": movie.rating, "ranking": movie.ranking, "review": movie.review, "img_url": movie.img_url})


    return render_template("index.html", movies_=movies)


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = QuickFormEdit()
    if form.validate_on_submit():
        _id = request.args.get("id")
        edit_ = Movie.query.filter_by(id=_id).first()
        edit_.rating = float(form.new_rating.data)
        edit_.review = form.new_review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form_=form)


@app.route("/delete")
def delete():
    _id = request.args.get("id")
    delete_ = Movie.query.filter_by(id=_id).delete()
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = QuickFormAdd()
    if form.validate_on_submit():
        new_title_ = form.new_title.data
        respond = requests.get(URL_, params={"api_key": API_KEY, "query": new_title_})
        data = respond.json()['results']
        return render_template('select.html', data_=data)

    return render_template("add.html", form_=form)


@app.route("/find")
def select():
    id_ = int(request.args.get("id"))
    title_ = request.args.get("title")
    respond = requests.get(URL_, params={"api_key": API_KEY, "query": title_})
    all_data = respond.json()
    results = all_data.get('results')
    for i in range(len(results)):
        if id_ == results[i]["id"]:
            new_movie_title = results[i]["title"]
            new_movie_img_url = "https://image.tmdb.org/t/p/w500/" + results[i]["poster_path"]
            new_movie_year = results[i]["release_date"]
            new_movie_description = results[i]["overview"]
    new_movie_year = int(new_movie_year.split('-')[0])
    add_new_movie = Movie(title=new_movie_title, year=new_movie_year, description=new_movie_description,
                          img_url=new_movie_img_url, rating=0, ranking=0, review="None")
    db.session.add(add_new_movie)
    db.session.commit()

    new_movie_ = Movie.query.filter_by(title=new_movie_title).first()

    return redirect(url_for('edit',id=new_movie_.id))


new_movie = Movie(title="Phone Booth", year=2002,
                      description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
                      rating=7.3,
                      ranking=10,
                      review="My favourite character was the caller.",
                      img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg")


if __name__ == '__main__':
    #db.session.add(new_movie)
    #db.session.commit()
    db.create_all()
    app.run(debug=True)
