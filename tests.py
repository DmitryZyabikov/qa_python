from main import BooksCollector
import pytest

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
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_valid_name_book_added(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        assert len(collector.get_books_genre()) == 1
        assert collector.get_books_genre().get('Властелин колец') == ''

    @pytest.mark.parametrize('name', ['', 'a' * 41])
    def test_add_new_book_invalid_length_not_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_duplicate_still_one(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_new_book('1984')
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_valid_genre_set(self):
        collector = BooksCollector()
        collector.add_new_book('Хоббит')
        collector.set_book_genre('Хоббит', 'Фантастика')
        assert collector.get_book_genre('Хоббит') == 'Фантастика'

    @pytest.mark.parametrize('genre', ['Неизвестный', ''])
    def test_set_book_genre_invalid_genre_unchanged(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', genre)
        assert collector.get_book_genre('Книга') == ''

    def test_set_book_genre_book_not_exists_no_change(self):
        collector = BooksCollector()
        collector.set_book_genre('Неизвестная книга', 'Фантастика')
        assert collector.get_books_genre() == {}

    def test_get_book_genre_existing_returns_genre_and_missing_returns_none(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Детективы')
        assert collector.get_book_genre('Книга') == 'Детективы'
        assert collector.get_book_genre('Отсутствует') is None

    def test_get_books_with_specific_genre_matches_and_no_matches(self):
        collector = BooksCollector()
        collector.add_new_book('Книга А')
        collector.add_new_book('Книга Б')
        collector.add_new_book('Книга В')
        collector.set_book_genre('Книга А', 'Комедии')
        collector.set_book_genre('Книга Б', 'Комедии')
        # Книга В без жанра
        assert collector.get_books_with_specific_genre('Комедии') == ['Книга А', 'Книга Б']
        assert collector.get_books_with_specific_genre('Фантастика') == []

    def test_get_books_genre_returns_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        expected = {'Книга1': '', 'Книга2': ''}
        assert collector.get_books_genre() == expected

    def test_get_books_for_children_returns_only_without_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Сказка')
        collector.add_new_book('Ужастик')
        collector.add_new_book('Детектив')
        collector.set_book_genre('Сказка', 'Мультфильмы')
        collector.set_book_genre('Ужастик', 'Ужасы')
        collector.set_book_genre('Детектив', 'Детективы')
        # Мультфильмы нет возрастного рейтинга, остальные есть
        assert collector.get_books_for_children() == ['Сказка']

    def test_add_book_in_favorites_added(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        assert collector.get_list_of_favorites_books() == ['Книга']

    def test_add_book_in_favorites_duplicate_still_one(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.add_book_in_favorites('Книга')
        assert collector.get_list_of_favorites_books() == ['Книга']

    def test_delete_book_from_favorites_removed(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.delete_book_from_favorites('Книга')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_returns_ordered_list(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        collector.add_book_in_favorites('Книга1')
        collector.add_book_in_favorites('Книга2')
        assert collector.get_list_of_favorites_books() == ['Книга1', 'Книга2']