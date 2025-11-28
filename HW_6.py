class Book:
    """Класс, описывающий книгу."""

    def __init__(self, title: str="NA", author: str="NA", pages: int=None) -> None:
        """Конструктор класса.

        Args:
            title: Название книги.
            author: Автор книги.
            pages: Количество страниц в книге.
        """

        self.__title = title
        self.__author = author
        self.__pages = pages

        if pages <= 0:
            print('Количество страниц должно быть натуральным числом. Установлено значение 1.')
            self.__pages = 1

    def get_title(self) -> str:
        """Геттер для названия книги.

        Returns:
            title: Название книги.
        """

        return self.__title

    def get_author(self) -> str:
        """Геттер для автора книги.

        Returns:
            author: Автор книги.
        """

        return self.__author

    def get_pages(self) -> int:
        """Геттер для количества страниц книги.

        Returns:
            pages: Кол-во страниц книги.
        """

        return self.__pages

    def set_title(self, title: str) -> None:
        """Сеттер для названия книги.

        Args:
            title: Название книги.
        """

        self.__title = title

    def set_author(self, author: str) -> None:
        """Сеттер для автора книги.

        Args:
            author: Автор книги.
        """

        self.__author = author

    def set_pages(self, pages: int) -> None:
        """Сеттер для количества страниц книги.

        Args:
            pages: Количество страниц книги.
         """

        if pages > 0:
            self.__pages = pages
        else:
            print('Количество страниц должно быть натуральным числом. Установлено значение 1.')
            self.__pages = 1

    def show(self) -> None:
        """Вывод полной информации о книге."""

        print(f"Название: {self.__title}, Автор: {self.__author}, Количество страниц: {self.__pages}")

    def book_thickness(self) -> bool:
        """Проверка толщины книги."""

        if self.__pages < 100:
            thickness="тонкая"
        elif self.__pages < 350:
            thickness="средняя"
        else:
            thickness="толстая"

        return(thickness)

    def popular_authors(self) -> bool:
        """Проверка популярости автора."""

        popular = ['Лев Николаевич Толстой', 'Уильям Шекспир', 'Фёдор Михайлович Достоевский', 'Александр Сергеевич Пушкин']

        if self.__author in popular:
            popular_author='популярный автор'
        else:
            popular_author='непопулярный автор'

        return popular_author


class Menu:
    """Класс для работы пользовательского меню."""

    def print_menu(self):
        """Вывод пунктов главного пользовательского меню."""

        print('МЕНЮ\n',
              '1. Показать полную информацию о книге\n',
              '2. Показать автора книги\n',
              '3. Показать название книги\n',
              '4. Показать количество страниц в книге\n',
              '5. Определить толщину книги\n',
              '6. Определить является ли автор книги популярным\n',
              '7. Изменить автора книги\n',
              '8. Изменить название книги\n',
              '9. Изменить количество страниц в книге\n',
              '10. ВЫЙТИ\n')

    def main_menu(self, choise: int, some_book: Book) -> bool:
        """Главное пользовательское меню.

        Args:
            choise: Выбор пользователя.

        Returns:
            is_running: Продолжается ли работа программы.

        """

        is_running = True

        match choise:
            case 10:
                is_running = False
            case 1:
                print(some_book.show())
            case 2:
                print(some_book.get_author())
            case 3:
                print(some_book.get_title())
            case 4:
                print(some_book.get_pages())
            case 5:
                print(some_book.book_thickness())
            case 6:
                print(some_book.popular_authors())
            case 7:
                new_author = input("Введите ФИО нового автора: ")

                print(some_book.set_author(new_author))
            case 8:
                new_title = input("Введите новое название книги: ")

                print(some_book.set_title(new_title))
            case 9:
                new_pages = int(input("Введите новое количество страниц: "))

                print(some_book.set_pages(new_pages))
            case _:
                print("Неверный выбор. Такго пункта не существует. Попробуйте еще раз.")

        return is_running


class Main:

    def run() -> None:
        """Метод запуска работы."""

        book_1 = Book("Вафельное сердце", "Мария Парр", 240)
        book_2 = Book("Евгений Онегин", "Александр Сергеевич Пушкин", 320)

        print("Создано 2 книги:")
        print('1:')
        book_1.show()
        print('2:')
        book_2.show()

        is_running = True

        menu = Menu()

        while (is_running):
            menu.print_menu()

            choise = int(input('Введите пункт меню >>> '))
            choise_book = int(input('Выберите книгу 1 или 2: '))
            book = book_1 if choise_book == 1 else book_2

            is_running = menu.main_menu(choise, book)

    run()