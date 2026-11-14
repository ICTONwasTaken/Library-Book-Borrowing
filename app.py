from flask import Flask, jsonify

app = Flask(__name__)

books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien" , "available": False},
    {"id": 2, "title": "Pride and Prejudice", "author": "Jane Austen", "available": False},
    {"id": 3, "title": "Noli Me Tangere", "author": "Jose Rizal", "available": False}
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
