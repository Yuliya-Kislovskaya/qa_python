from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    
    def test_add_new_book_length_more_40(self):
        collector = BooksCollector()
        collector.add_new_book('абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёж')
        assert "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёж" not in collector.books_genre

    def test_add_new_book_length_is_0(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert "" not in collector.books_genre

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_init_all_genre_exist(self, genre):
        collector = BooksCollector()
        assert genre in collector.genre
    
    def test_set_book_genre_genre_from_list_set_ok(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_set_book_genre_genre_out_of_list_not_set(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Дорама')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    def test_get_books_for_children_list_is_not_empty(self):
        collector = BooksCollector()
        collector.add_new_book('Зверополис')
        collector.set_book_genre('Зверополис', 'Мультфильмы')
        assert 'Зверополис' in collector.get_books_for_children()

    def test_get_books_for_children_list_is_empty(self):
        collector = BooksCollector()
        collector.add_new_book('Звонок')
        collector.set_book_genre('Звонок', 'Ужасы')
        assert 'Звонок' not in collector.get_books_for_children()

    def test_add_book_in_favorites_add_book_one_more_time_not_possible(self, collector_book):
        collector_book.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector_book.add_book_in_favorites('Шерлок Холмс')
        collector_book.add_book_in_favorites('Шерлок Холмс')
        assert len(collector_book.get_list_of_favorites_books()) == 2    

    def test_delete_book_from_favorites_remove_book_possible(self, collector_book):
        collector_book.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector_book.add_book_in_favorites('Шерлок Холмс')
        collector_book.delete_book_from_favorites('Шерлок Холмс')
        fav_book = collector_book.get_list_of_favorites_books()
        assert 'Шерлок Холмс' not in fav_book

    def test_get_list_of_favorites_books_return_list_of_favorites_books_ok(self, collector_book):
        collector_book.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector_book.add_book_in_favorites('Звонок')
        assert len(collector_book.get_list_of_favorites_books()) == 2  
