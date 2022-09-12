from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

API_KEY = "oguzkaganbilici"

##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(1500), nullable=False)
    img_url = db.Column(db.String(1500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def random():
    if request.method == "GET":
        all_cafes = db.session.query(Cafe).all()
        random_cafe = choice(all_cafes)
        return jsonify(id=random_cafe.id, name=random_cafe.name, map_url=random_cafe.map_url,
                       img_url=random_cafe.img_url, location=random_cafe.location, seats=random_cafe.seats,
                       has_toilet=random_cafe.has_toilet, has_wifi=random_cafe.has_wifi,
                       has_sockets=random_cafe.has_sockets, can_take_calls=random_cafe.can_take_calls,
                       coffee_price=random_cafe.coffee_price)


@app.route("/all", methods=["GET"])
def all():
    if request.method == "GET":
        all_cafes = db.session.query(Cafe).all()
        cafes_dict = []
        for cafes in all_cafes:
            cafes_dict.append({"name": cafes.name, "map_url": cafes.map_url, "img_url": cafes.img_url,
                                    "location": cafes.location, "seats": cafes.seats, "has_toilet": cafes.has_toilet,
                                    "has_wifi": cafes.has_wifi, "has_sockets": cafes.has_sockets,
                                    "can_take_calls": cafes.can_take_calls, "coffee_price": cafes.coffee_price})
        return jsonify(cafes_dict)

@app.route("/search")
def search():
    loc = request.args.get("loc") #url'deki loc kısmını alır
    current_loc = db.session.query(Cafe).filter_by(location=loc).first()
    if current_loc:
        return jsonify(id=current_loc.id, name=current_loc.name, map_url=current_loc.map_url,
                       img_url=current_loc.img_url, location=current_loc.location, seats=current_loc.seats,
                       has_toilet=current_loc.has_toilet, has_wifi=current_loc.has_wifi,
                       has_sockets=current_loc.has_sockets, can_take_calls=current_loc.can_take_calls,
                       coffee_price=current_loc.coffee_price)
    else:
        return jsonify(error={"Not found": "Sorry, we don't have a cafe at that location"})


@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(name=request.form.get("name"), map_url=request.form.get("map_url"),
                    img_url=request.form.get("img_url"), location=request.form.get("loc"),
                    seats=request.form.get("seats"), has_toilet=int(request.form.get("has_toilet")),
                    has_wifi=int(request.form.get("has_wifi")), has_sockets=int(request.form.get("has_sockets")),
                    can_take_calls=int(request.form.get("can_take_calls")), coffee_price=request.form.get("coffee_price"))

    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"Success": "Successfully added the new cafe!"})


@app.route('/update-price/<cafe_id>', methods=["PATCH"])
def update(cafe_id):
    new_price_ = request.args.get("new_price")
    cafe = db.session.query(Cafe).filter_by(id=cafe_id).first()
    if cafe:
        cafe.coffee_price = new_price_
        db.session.commit()
        return jsonify(Cafe={"Price": "Price is updated."})
    else:
        return jsonify(Cafe={"Cafe": "Cafe couldn't be found ."})


@app.route("/report-closed/<cafe_id>", methods=["GET","DELETE"])
def delete(cafe_id):
    api_key_ = request.args.get("api_key")
    if api_key_ == API_KEY:
        delete_cafe_ = db.session.query(Cafe).filter_by(id=cafe_id).first()
        if delete_cafe_:
            db.session.query(Cafe).filter_by(id=cafe_id).delete()
            db.session.commit()
            return jsonify(response={"Successful": "Cafe is deleted successfully"})
        else:
            return jsonify(response={"Failed": "Cafe ID couldn't be found"})
    else:
        return jsonify(response={"Failed": "API is not true"})


#https://documenter.getpostman.com/view/23233986/VVBZQjVV postman document link


if __name__ == '__main__':
    app.run(debug=True)
