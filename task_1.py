"""
Hw1
"""

class MainClass:
    def __init__(self, text=''):
        """
        Конструктор главного класса.

        :param text: Текстовое значение для поля _text.
        """
        self._text = text

    def set_text(self, text=''):
        """
        Метод для установки значения текстового поля _text.

        :param text: Текстовое значение.
        """
        self._text = text

    def display_info(self):
        """
        Метод для отображения информации из текстового поля _text.
        """
        print(f"Text in MainClass: {self._text}")


class ChildClass(MainClass):
    def __init__(self, text='', number=None):
        """
        Конструктор класса-потомка.

        :param text: Текстовое значение для поля _text.
        :param number: Числовое значение для поля _number.
        """
        super().__init__(text)
        self._number = number

    def set_number(self, number):
        """
        Метод для установки значения числового поля _number.

        :param number: Числовое значение.
        """
        self._number = number

    def display_info(self):
        """
        Метод для отображения информации из полей _text и _number.
        """
        super().display_info()
        print(f"Number in ChildClass: {self._number}")


if __name__ == "__main__":
    main_obj = MainClass("Hello, I am in the main class!")
    main_obj.display_info()

    child_obj = ChildClass("Hi, I am in the child class!", 42)
    child_obj.display_info()
