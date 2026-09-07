import pytest
from main import BooksCollector


class TestBooksCollector:


    def test_add_new_book_add_two_books(self):

        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2 #исправил метод на существующий



    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_add_valid_genre(self, genre):

        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', genre)

        assert collector.get_book_genre('Гарри Поттер') == genre


    @pytest.mark.parametrize('genre', ['Чушь', 'Si-Fi', '', 123, ''])
    def test_set_book_genre_add_invalid_genre(self, genre):

        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер',genre)

        assert collector.get_book_genre('Гарри Поттер') == ''



    def test_get_books_with_specific_genre_add_three_books_return_two_books_name(self):

        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Убийство в восточном экспрессе')
        collector.set_book_genre('Гарри Поттер','Фантастика')
        collector.set_book_genre('Властелин колец','Фантастика')
        collector.set_book_genre('Убийство в восточном экспрессе','Детективы')
        
        assert collector.get_books_with_specific_genre('Фантастика') == ['Гарри Поттер', 'Властелин колец']


    def test_get_books_genre_empty_list(self):

        collector = BooksCollector()

        assert collector.get_books_genre() == {}

        

    def test_get_books_genre_add_three_books_return_three_books(self):

        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Убийство в восточном экспрессе')
        collector.set_book_genre('Гарри Поттер','Фантастика')
        collector.set_book_genre('Властелин колец','Фантастика')
        collector.set_book_genre('Убийство в восточном экспрессе','Детективы')

        assert collector.get_books_genre() == {'Гарри Поттер': 'Фантастика', 'Властелин колец': 'Фантастика', 'Убийство в восточном экспрессе': 'Детективы'}


    def test_get_books_for_children_add_three_books_return_one(self):

        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Зов ктулху')
        collector.add_new_book('Убийство в восточном экспрессе')
        collector.set_book_genre('Гарри Поттер','Фантастика')
        collector.set_book_genre('Зов ктулху','Ужасы')
        collector.set_book_genre('Убийство в восточном экспрессе','Детективы')

        assert collector.get_books_for_children() == ['Гарри Поттер']

    def test_add_book_in_favorites_add_two_books_return_one_book(self):

        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Зов ктулху')
        collector.add_book_in_favorites('Гарри Поттер')

        assert collector.get_list_of_favorites_books() == ['Гарри Поттер']


    def test_delete_book_from_favorites_add_two_books_in_list_return_one_book(self):

        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Зов ктулху')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Зов ктулху')
        collector.delete_book_from_favorites('Гарри Поттер')

        assert collector.get_list_of_favorites_books() == ['Зов ктулху']


    def test_get_list_of_favorites_books_empty_list(self):

        collector = BooksCollector()

        assert collector.get_list_of_favorites_books() == []