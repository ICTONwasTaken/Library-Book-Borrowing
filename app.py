
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample book records
books = [
    {
        "id": 1,
        "title": "Introduction to Python",
        "available": True
    },
    {
        "id": 2,
        "title": "The Great Gatsby",
        "available": True
    },
    {
        "id": 3,
        "title": "Noli Me Tangere",
        "available": False
    }
]

# Homepage
@app.route("/")
def home():
    return "Hello, Flask!"


# Add a new book
@app.route("/books/<int:book_id>/add", methods=["POST"])
def add_book(book_id):

    data = request.get_json(silent=True) or {}

    title = data.get("title")

    if not title:
        return jsonify({
            "error": "Book title is required"
        }), 400

    for book in books:
        if book["id"] == book_id:
            return jsonify({
                "error": "Book ID already exists"
            }), 409

    new_book = {
        "id": book_id,
        "title": title,
        "available": True
    }

    books.append(new_book)

    return jsonify({
        "book_id": new_book["id"],
        "title": new_book["title"],
        "available": new_book["available"]
    }), 201


if __name__ == "__main__":
    app.run(debug=True)
