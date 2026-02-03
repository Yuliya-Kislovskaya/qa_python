import pytest
from main import BooksCollector


@pytest.fixture
def collector_book():
    collector_book = BooksCollector()
    collector_book.add_new_book('Гордость и предубеждение и зомби')
    collector_book.add_new_book('Шерлок Холмс')
    collector_book.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
    collector_book.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
    collector_book.set_book_genre('Шерлок Холмс', 'Детективы')
    return collector_book
