1. test_add_new_book_add_two_books – пример из шаблона, добавляет две книги и проверяет, что их две.
2. test_add_new_book_valid_name_book_added – проверяем, что правильное название добавляется и жанр пустой.
3. test_add_new_book_invalid_length_not_added – с помощью параметризации проверяем, что пустая строка и слишком длинное название (>40) не добавляются.
4. test_add_new_book_duplicate_still_one – убеждаемся, что добавить одну и ту же книгу дважды нельзя.
5. test_set_book_genre_valid_genre_set – задаём существующую книгу допустимый жанр и проверяем, что он установился.
6. test_set_book_genre_invalid_genre_unchanged – параметризуем недопустимые жанры и смотрим, что жанр не меняется.
7. test_set_book_genre_book_not_exists_no_change – пытаемся задать жанр книге, которой нет в списке, и проверяем, что словарь не изменился.
8. test_get_book_genre_existing_returns_genre_and_missing_returns_none – получаем жанр у существующей книги и проверяем, что возвращается правильное значение; у отсутствующей книги должно быть None.
9. test_get_books_with_specific_genre_matches_and_no_matches – добавляем несколько книг с разными жанрами и смотрим, что функция возвращает только те, что нужны.
10. test_get_books_genre_returns_dict – проверяем, что возвращается весь словарь books_genre.
11. test_get_books_for_children_returns_only_without_rating – добавляем книги с жанрами, у некоторых есть возрастной рейтинг (Ужасы, Детективы), а у некоторых нет, и проверяем, что возвращаются только те, что без рейтинга.
12. test_add_book_in_favorites_added – добавляем книгу в избранное и проверяем, что она там есть.
13. test_add_book_in_favorites_duplicate_still_one – пытаемся добавить одну и ту же книгу дважды в избранное, убеждаемся, что она там только один раз.
14. test_delete_book_from_favorites_removed – добавляем в избранное, потом удаляем и проверяем, что список пуст.
15. test_get_list_of_favorites_books_returns_ordered_list – добавляем две книги в избранное и проверяем, что список возвращается правильно.