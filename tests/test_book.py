from lib.book import Book

"""
When we init a Book object
And provide id, title, author_name arguments
It creates a new instance of Book
"""
def test_can_construct_book():
    book = Book(0, "", "")

"""
When we init a Book object
And provide id, title, author_name arguments
It creates a new instance of Book with the appropriate values set for the matching attributes
"""
def test_book_constructs_with_correct_values():
    book = Book(1, "A book title", "Name of an author")
    assert book.id == 1
    assert book.title == "A book title"
    assert book.author_name == "Name of an author"

"""
When we compare two identical books
They are considered as equal (using ==)
"""
def test_identical_books_compare_equal():
    book_1 = Book(1, "A book title", "Name of an author")
    book_2 = Book(1, "A book title", "Name of an author")
    assert book_1 == book_2

"""
When we compare two non-identical books
They are considered as not equal (using ==)
"""
def test_non_identical_books_compare_nonequal():
    my_book = Book(1, "A book title", "Name of an author")
    other_books = [
        Book(2, "A book title", "Name of an author"),
        Book(1, "A different book title", "Name of an author"),
        Book(1, "A book title", "Name of a different author"),
    ]
    for other_book in other_books:
        assert my_book != other_book

"""
Book string formatting is correct, having form:
    Book(<id>, <title>, <author_name>)
"""
def test_album_string_formats_correctly():
    books = [
        Book(1, "A book title", "Name of an author"),
        Book(2, "A book title", "Name of an author"),
        Book(1, "A different book title", "Name of an author"),
        Book(1, "A book title", "Name of a different author"),
    ]
    representations = [
        str(book)
        for book in books
    ]
    assert representations == [
        "Book(1, A book title, Name of an author)",
        "Book(2, A book title, Name of an author)",
        "Book(1, A different book title, Name of an author)",
        "Book(1, A book title, Name of a different author)",
    ]
