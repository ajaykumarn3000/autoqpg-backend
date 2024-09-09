from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

data = {
    "title": "Mid Semester Evaluation",
    "acad_year": "2024-2025",
    "department": "Information Technology",
    "year": "TE",
    "semester": "V",
    "course": "Advanced Data Structures and Analysis",
    "time": "10:00 AM to 11:00 AM",
    "date": "31 August 2024",
    "total_pages": 1,
    "total_marks": 20,
    "instructions": "Candidates should read carefully the instructions printed on the question paper and on the cover of the Answer Book, which is provided for their use",
    "note": [
        "Attempt any two questions. Each question is of 10/7.5 marks. Attempt all sub-parts of a given question.",
        "Draw neat diagrams wherever necessary.",
        "Write everything in ink (no pencil) only.",
        "Assume data, if missing, with justification.",
    ],
    "questions": [
        [
            {
                "question": "Explain the concept of AVL trees. Construct an AVL tree for the following set of keys: 10, 20, 30, 40, 50, 25.",
                "marks": 3,
                "co": 1,
                "bl": 2,
                "dl": "H",
            },
            {
                "question": "Explain the concept of AVL trees. Construct an AVL tree for the following set of keys: 10, 20, 30, 40, 50, 25.",
                "marks": 3,
                "co": 1,
                "bl": 2,
                "dl": "H",
            },
        ],
        [
            {
                "question": "Explain the concept of AVL trees. Construct an AVL tree for the following set of keys: 10, 20, 30, 40, 50, 25.",
                "marks": 3,
                "co": 1,
                "bl": 2,
                "dl": "H",
            },
            {
                "question": "Explain the concept of AVL trees. Construct an AVL tree for the following set of keys: 10, 20, 30, 40, 50, 25.",
                "marks": 3,
                "co": 1,
                "bl": 2,
                "dl": "H",
            },
        ],
        [
            {
                "question": "Explain the concept of AVL trees. Construct an AVL tree for the following set of keys: 10, 20, 30, 40, 50, 25.",
                "marks": 3,
                "co": 1,
                "bl": 2,
                "dl": "H",
            },
            {
                "question": "Explain the concept of AVL trees. Construct an AVL tree for the following set of keys: 10, 20, 30, 40, 50, 25.",
                "marks": 3,
                "co": 1,
                "bl": 2,
                "dl": "H",
            },
        ],
        [
            {
                "question": "Explain the concept of AVL trees. Construct an AVL tree for the following set of keys: 10, 20, 30, 40, 50, 25.",
                "marks": 3,
                "co": 1,
                "bl": 2,
                "dl": "H",
            },
            {
                "question": "Explain the concept of AVL trees. Construct an AVL tree for the following set of keys: 10, 20, 30, 40, 50, 25.",
                "marks": 3,
                "co": 1,
                "bl": 2,
                "dl": "H",
            },
        ],
        [
            {
                "question": "Explain the concept of AVL trees. Construct an AVL tree for the following set of keys: 10, 20, 30, 40, 50, 25.",
                "marks": 3,
                "co": 1,
                "bl": 2,
                "dl": "H",
            },
            {
                "question": "Explain the concept of AVL trees. Construct an AVL tree for the following set of keys: 10, 20, 30, 40, 50, 25.",
                "marks": 3,
                "co": 1,
                "bl": 2,
                "dl": "H",
            },
        ],
        [
            {
                "question": "Explain the concept of AVL trees. Construct an AVL tree for the following set of keys: 10, 20, 30, 40, 50, 25.",
                "marks": 3,
                "co": 1,
                "bl": 2,
                "dl": "H",
            },
            {
                "question": "Explain the concept of AVL trees. Construct an AVL tree for the following set of keys: 10, 20, 30, 40, 50, 25.",
                "marks": 3,
                "co": 1,
                "bl": 2,
                "dl": "H",
            },
        ],
        [
            {
                "question": "Explain the concept of AVL trees. Construct an AVL tree for the following set of keys: 10, 20, 30, 40, 50, 25.",
                "marks": 3,
                "co": 1,
                "bl": 2,
                "dl": "H",
            },
            {
                "question": "Explain the concept of AVL trees. Construct an AVL tree for the following set of keys: 10, 20, 30, 40, 50, 25.",
                "marks": 3,
                "co": 1,
                "bl": 2,
                "dl": "H",
            },
        ],
        [
            {
                "question": "Explain the concept of AVL trees. Construct an AVL tree for the following set of keys: 10, 20, 30, 40, 50, 25.",
                "marks": 3,
                "co": 1,
                "bl": 2,
                "dl": "H",
            },
            {
                "question": "Explain the concept of AVL trees. Construct an AVL tree for the following set of keys: 10, 20, 30, 40, 50, 25.",
                "marks": 3,
                "co": 1,
                "bl": 2,
                "dl": "H",
            },
        ],
        [
            {
                "question": "Explain the concept of AVL trees. Construct an AVL tree for the following set of keys: 10, 20, 30, 40, 50, 25.",
                "marks": 3,
                "co": 1,
                "bl": 2,
                "dl": "H",
            },
            {
                "question": "Explain the concept of AVL trees. Construct an AVL tree for the following set of keys: 10, 20, 30, 40, 50, 25.",
                "marks": 3,
                "co": 1,
                "bl": 2,
                "dl": "H",
            },
        ],
    ],
}


@app.route("/")
def home():
    return render_template("paper.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
