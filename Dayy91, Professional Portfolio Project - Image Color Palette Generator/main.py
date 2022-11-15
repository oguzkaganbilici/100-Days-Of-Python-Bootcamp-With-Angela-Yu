import os.path
from flask import Flask, render_template, request
from colorthief import ColorThief

app = Flask(__name__)

UPLOAD_FOLDER = "C:\\Users\\061885\\Desktop\\Dayy91, Professional Portfolio Project - Image Color Palette Generator\\static\\images"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def image_processing(path, c_count=10):
    img = ColorThief(path)
    dominant_colors = img.get_color(quality=1)
    palette = img.get_palette(color_count=c_count)
    return dominant_colors, palette


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        img_path = "static/images/1.jpg"
        dominant, palette = image_processing(img_path)
        return render_template("index.html", dom=dominant, pal=palette, img=img_path)
    elif request.method == "POST":
        img = request.files["image"]
        color_count = request.form["colorCount"]
        img.save(os.path.join(app.config["UPLOAD_FOLDER"], "deneme.jpg"))
        img_path = "static/images/deneme.jpg"
        dominant, palette = image_processing(img_path, int(color_count))
        return render_template("index.html", dom=dominant, pal=palette, img=img_path)


if __name__ == "__main__":
    app.run(debug=True)
