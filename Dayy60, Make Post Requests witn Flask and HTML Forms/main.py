from flask import Flask, render_template,request
import requests, smtplib


datas = requests.get("https://api.npoint.io/af27b45139d3cff0ea15")
real_data = datas.json()
app = Flask(__name__)

MY_EMAIL = "delykurt@gmail.com"
MY_PASSWORD = "soscqgolxpzqprsb"

@app.route("/")
def home():
    return render_template("index.html", dict_=real_data)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", header_="Contact me")
    elif request.method == "POST":
        name = request.form["username"]
        email = request.form["email"].encode("utf-8")
        tel = request.form["tel"]
        message = request.form["message"].encode("utf-8")
        print(name)
        print(email)
        print(tel)
        print(message)
        #text = f"Name:{name}\nE-mail:{email}\nTel:{tel}Msg:{message}"
        text = f"Name:{request.form['username']}"
        with smtplib.SMTP("smtp.gmail.com", port=587) as mail:
            mail.starttls()
            mail.login(MY_EMAIL, MY_PASSWORD)
            mail.sendmail(from_addr=MY_EMAIL, to_addrs="oguzkaganbilici1@gmail.com",
            msg=f"From: \"My Website\" <{email}>\n" \
                f"To: {MY_EMAIL}\n" \
                f"Subject: Message from {name} via my Web Form\n\n" \
                f"{message}".encode("utf-8") )

        return render_template("contact.html", header_="Successfully sent your message")


@app.route("/post/<number>")
def post(number):
    title = real_data[int(number)-1]["title"]
    sub = real_data[int(number)-1]["subtitle"]
    body = real_data[int(number)-1]["body"]
    return render_template("post.html", title_=title, sub_=sub, body_=body)


if __name__ == "__main__":
    app.run(debug=True)