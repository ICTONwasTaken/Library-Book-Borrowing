from flask import Flask, jsonify

app = Flask(__name__)

books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 2, "title": "Pride and Prejudice", "author": "Jane Austen"},
]


@app.route("/")
def home():
    return "Library API"


@app.get("/books")
def get_books():
    return jsonify(books)


@app.get("/books/<int:book_id>")
def get_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book)


if __name__ == "__main__":
    app.run(debug=True)
