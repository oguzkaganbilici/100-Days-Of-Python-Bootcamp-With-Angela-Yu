from flask import Flask, render_template
import requests

respond = requests.get("https://api.npoint.io/4af156202f984d3464c3")
datas = respond.json()

app = Flask(__name__)

@app.route('/')
def home():
    nums = []
    for i in datas:
        nums.append(int(i['id']))
    return render_template("index.html", nums_=nums)

@app.route('/post/<num>')
def blog(num):
    infos = datas[int(num)]

    return render_template("post.html", infos_=infos)


if __name__ == "__main__":
    app.run(debug=True)
