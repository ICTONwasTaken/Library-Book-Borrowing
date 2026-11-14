
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


# Homepage
@app.route("/")
def home():
    return "Hello, Flask!"


# Add a new book
@app.route("/books/<int:book_id>/add", methods=["POST"])
def add_book(book_id):

    # Receive JSON data from the client
    data = request.get_json(silent=True) or {}

    # Extract book information
    title = data.get("title")
    author = data.get("author")

    # Validate required information
    if not isinstance(title, str) or not title.strip():
        return jsonify({
            "error": "Book title is required"
        }), 400

    if not isinstance(author, str) or not author.strip():
        return jsonify({
            "error": "Book author is required"
        }), 400

    # Check whether the book ID already exists
    for book in books:
        if book["id"] == book_id:
            return jsonify({
                "error": "Book ID already exists"
            }), 409

    # Create a new book record
    new_book = {
        "id": book_id,
        "title": title.strip(),
        "author": author.strip(),
        "available": True
    }

    # Add the new book to the collection
    books.append(new_book)

    # Return the newly added book
    return jsonify({
        "book_id": new_book["id"],
        "title": new_book["title"],
        "author": new_book["author"],
        "available": new_book["available"]
    }), 201


if __name__ == "__main__":
    app.run(debug=True)
