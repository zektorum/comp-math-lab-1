class WrongRowsNumberException(Exception):
    """ Исключение вызывается, если пользователь ввёл строку с некорректным числом элементов."""
    pass


class WrongStringTypeException(Exception):
    """ Исключение вызывается, если файл содержит байтовые строки вместо обычных. """
    pass
