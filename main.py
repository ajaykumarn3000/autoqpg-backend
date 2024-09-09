from flask import Flask, request, jsonify, render_template
import os
from docs_reader import read_docs
from Blooms import get_taxonomy_level

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "cache"

os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "GET":
        return render_template("upload.html")

    file = request.files["file"]

    if file and file.filename.endswith(".docx"):
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(file_path)
        data = read_docs(file_path)
        print(data)
        os.remove(file_path)

        for question in data:
            ques_text = " ".join(question["para"])
            question["bl"] = get_taxonomy_level(ques_text)
        return jsonify(data)


@app.route("/generate", methods=["POST"])
def generate():
    return jsonify({"message": "Generated successfully"})


if __name__ == "__main__":
    app.run(debug=True)
