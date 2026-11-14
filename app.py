from flask import Flask, jsonify

app = Flask(__name__)

books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 2, "title": "Pride and Prejudice", "author": "Jane Austen"},
]

@app.get("/")
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


@app.put("/books/<int:id>/<action>")
def update_book(id, action):

    for book in books:
        if book["id"] == id:

            if action == "borrow":
                book["available"] = False

            elif action == "return":
                book["available"] = True

            else:
                return jsonify({
                    "error": "Invalid action"
                }), 400

            return jsonify({
                "message": "Book updated successfully",
                "book": book
            }), 200

    return jsonify({
        "error": "Book not found"
    }), 404


@app.delete("/books/<int:id>/delete")
def delete_book(id):

    for book in books:
        if book["id"] == id:
            books.remove(book)

            return jsonify({
                "message": "Book deleted successfully"
            }), 200

    return jsonify({
        "error": "Book not found"
    }), 404


if __name__ == "__main__":
    app.run(debug=True)
