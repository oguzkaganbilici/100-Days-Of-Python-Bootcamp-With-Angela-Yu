from flask import Flask, render_template
import requests


datas = requests.get("https://api.npoint.io/af27b45139d3cff0ea15")
real_data = datas.json()
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", dict_=real_data)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<number>")
def post(number):
    title = real_data[int(number)-1]["title"]
    sub = real_data[int(number)-1]["subtitle"]
    body = real_data[int(number)-1]["body"]
    return render_template("post.html", title_=title, sub_=sub, body_=body)


if __name__ == "__main__":
    app.run(debug=True)