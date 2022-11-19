import dict
from flask import Flask, render_template, request,redirect

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        word = request.form["word"]
        meaning = dict.search(word)
        if "error" not in meaning:
            definition = meaning["results"][0]["lexicalEntries"]
            try:
                synonyms = meaning["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["synonyms"]
                phrases = meaning["results"][0]["lexicalEntries"][0]["phrases"]
                return render_template("word.html", word_=word, def_=definition, syn_=synonyms, phr_=phrases)
            except:
                return render_template("word.html", word_=word, def_=definition, syn_=None, phr_=None)
        else:
            return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
