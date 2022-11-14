from flask import Flask, render_template, request
from colorthief import ColorThief

app = Flask(__name__)
img_path = "images/1.jpg"


def image_processing(path=img_path):
    img = ColorThief(path)
    dominant_colors = img.get_color(quality=1)
    palette = img.get_palette(color_count=10)
    return dominant_colors, palette


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        dominant, palette = image_processing()
        return render_template("index.html", dom=dominant, pal=palette)
    elif request.method == "POST":
        print("post part")
        img = request.files["image"]
        img.save(dst="T:\\Puantaj Tabloları")
        dominant, palette = image_processing(img_path)
        return render_template("index.html", dom=dominant, pal=palette )


if __name__ == "__main__":
    app.run(debug=True)
