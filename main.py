from flask import Flask, request, jsonify, render_template, send_file
import os
from docx_utils.docx_reader import read_docx
from Blooms import get_taxonomy_level
from docx_utils.generate_docx import generate_docx
from temp.data import data

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
        file_data = read_docx(file_path)
        os.remove(file_path)

        for question in file_data:
            question["image"] = []
            ques_text = " ".join(question["para"])
            question["bl"] = get_taxonomy_level(ques_text)
        return jsonify(data)


@app.route("/generate", methods=["GET"])
def generate():
    file_path = "cache/generated.docx"
    generate_docx(data, file_path)
    return send_file(file_path, mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document", as_attachment=True, download_name="generated.docx")

if __name__ == "__main__":
    app.run(debug=True)
