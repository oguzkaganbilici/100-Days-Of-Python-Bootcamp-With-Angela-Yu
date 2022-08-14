from flask import Flask, render_template
import requests

respond = requests.get("https://api.npoint.io/4af156202f984d3464c3")
datas = respond.json()

app = Flask(__name__)

@app.route('/')
def home():
    respond = requests.get("https://api.npoint.io/4af156202f984d3464c3")
    datas = respond.json()
    nums = []
    for i in datas:
        nums.append(i['id'])
    return render_template("index.html",)

@app.route('/post/')
def blog():
    return render_template("post.html")


if __name__ == "__main__":
    app.run(debug=True)
