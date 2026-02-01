# qa_python В данном проекте написаны тесты для приложения BooksCollector, позволяющего установит жанр книги и добавлять их в избранное. 

# Описание тестов:
1.test_add_new_book_invalid_length_more_40
   Проверяет, что книга с названием более 40 символов не добавляется в коллекцию.

2.test_add_new_book_invalid_length_is_0
   Проверяет, что книга с названием длиной 0 символов не добавляется в коллекцию.

3.test_init_all_genre_exist
   Проверяет наличие у созданного объекта класса всех жанров

4.test_set_book_genre_genre_from_list_set_ok
   Проверяет установку жанра книги

5.test_set_book_genre_genre_out_of_list_not_set
   Проверяет невозможность установки несуществующего жанра
  
6.test_get_books_for_children_list_is_not_empty
   Проверяет, что книги с детскими жанрами корректно возвращаются.

7.test_get_books_for_children_list_is_empty
   Проверяет, что список книг для детей пуст, если жанры всех книг имеют возрастное ограничение.

8.test_add_book_in_favorites_add_book_one_more_time_not_possible
   Проверяет невозможность добавления в избранное книги, которая там уже есть

9.test_delete_book_from_favorites_remove_book_possible
   Проверяет возможность удаления книги из избранного

10.test_get_list_of_favorites_books_return_list_of_favorites_books_ok   
    Проверка вывода списка избранного
   
