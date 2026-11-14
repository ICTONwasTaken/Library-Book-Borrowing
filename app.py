
from flask import Flask, request, jsonify

app = Flask(__name__)

# Initial book records
books = [
    {
        "id": 1,
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "available": True
    },
    {
        "id": 2,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "available": True
    },
    {
        "id": 3,
        "title": "Noli Me Tangere",
        "author": "Jose Rizal",
        "available": False
    }
]


@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/books/<int:book_id>/add", methods=["POST"])
def add_book(book_id):

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "error": "Request body must be a valid JSON object"
        }), 400

    title = data.get("title")
    author = data.get("author")

    if not isinstance(title, str) or not title.strip():
        return jsonify({
            "error": "Book title is required"
        }), 400

    if not isinstance(author, str) or not author.strip():
        return jsonify({
            "error": "Book author is required"
        }), 400

    for book in books:
        if book["id"] == book_id:
            return jsonify({
                "error": "Book ID already exists"
            }), 409

    new_book = {
        "id": book_id,
        "title": title.strip(),
        "author": author.strip(),
        "available": True
    }

    books.append(new_book)

    return jsonify({
        "id": new_book["id"],
        "title": new_book["title"],
        "author": new_book["author"],
        "available": new_book["available"]
    }), 201


if __name__ == "__main__":
    app.run(debug=True)
