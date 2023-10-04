from lib.book_repository import BookRepository
from lib.book import Book

"""
When we call BookRepository.all
It returns a list of Book objects reflecting the seed data
"""
def test_get_all_records(db_connection):
    db_connection.seed("seeds/book_store.sql")
    book_repo = BookRepository(db_connection)
    books = book_repo.all()
    assert books == [
        Book(1, "Nineteen Eighty-Four", "George Orwell"),
        Book(2, "Mrs Dalloway", "Virginia Woolf"),
        Book(3, "Emma", "Jane Austen"),
        Book(4, "Dracula", "Bram Stoker"),
        Book(5, "The Age of Innocence", "Edith Wharton"),
    ]
