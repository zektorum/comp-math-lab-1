from abc import ABC, abstractmethod
from decimal import Decimal
from enum import Enum
from typing import Any

from math_package.configuration import ERR, OUT
from math_package.io.exception import WrongRowsNumberException, WrongStringTypeException
from math_package.matrix import Matrix


class InputType(Enum):
    KEYBOARD = 1
    FILE = 2


class MatrixReader:
    def __init__(self, input_type: InputType):
        self.input_type = input_type
        self.matrix_readers = {
            InputType.KEYBOARD: MatrixReaderFromKeyboard,
            InputType.FILE: MatrixReaderFromFile
        }

    def read_raw_matrix(self) -> list[str]:
        matrix_reader = self.matrix_readers.get(self.input_type)()
        return matrix_reader.read()

    def process_raw_matrix(self, raw_matrix: list[Any]) -> Matrix:
        for i in range(len(raw_matrix)):
            for j in range(len(raw_matrix[0])):
                raw_matrix[i][j] = Decimal(raw_matrix[i][j])
        return Matrix(raw_matrix)

    def read(self) -> Matrix:
        raw_matrix = self.read_raw_matrix()
        return self.process_raw_matrix(raw_matrix)


class RawMatrixReader(ABC):
    @abstractmethod
    def read(self) -> list[Any]:
        pass


class MatrixReaderFromFile(RawMatrixReader):
    def read(self) -> list[Any]:
        """ Возвращает считанную с из файла матрицу в виде массива строк.
        Первая строка файла должна содержать количество строк, вторая - столбцов.

        :return: список состоящий из строк матрицы
        """
        print("Введите имя файла: ", file=OUT)
        filename = input()

        try:
            raw_matrix = []
            lines = []
            with open(filename, "r") as file:
                lines = file.readlines()
                if lines is bytes:
                    raise WrongStringTypeException

            lines_count, rows_count = int(lines[0]), int(lines[1])
            lines = lines[2:]
            for i in range(lines_count):
                current_line = lines[i].strip().split()
                if len(current_line) != rows_count:
                    raise WrongRowsNumberException
                raw_matrix.append(current_line)
            return raw_matrix
        except FileNotFoundError:
            print("Ошибка! Файл не найден", file=ERR)
            return []
        except WrongStringTypeException:
            print("Ошибка! В строке введено некорректное число элементов", file=ERR)
            return []
        except (ValueError, WrongRowsNumberException):
            print("Ошибка! Введите корректные количество строк и столбцов", file=ERR)
            return []


class MatrixReaderFromKeyboard(RawMatrixReader):
    def read(self) -> list[Any]:
        """ Возвращает считанную с клавиатуры матрицу в виде массива строк.

        :return: список состоящий из строк матрицы
        """
        hint = "Введите количество {}:"
        try:
            print(hint.format("строк"), file=OUT)
            rows_count = input()

            print(hint.format("столбцов"), file=OUT)
            lines_count = input()

            if not (rows_count.isdecimal() or lines_count.isdecimal()):
                raise ValueError
            rows_count, lines_count = int(rows_count), int(lines_count)

            print("Введите матрицу:", file=OUT)
            raw_matrix = []
            for i in range(lines_count):
                current_line = input().strip().split()
                if len(current_line) != rows_count:
                    raise WrongRowsNumberException
                raw_matrix.append(current_line)
            return raw_matrix

        except ValueError:
            print("Ошибка! Введите целые числа в десятичной системе счисления", file=ERR)
            return []
        except WrongRowsNumberException:
            print("Ошибка! В строке введено некорректное число элементов", file=ERR)
            return []


class RawMatrixPrinter:
    @staticmethod
    def print(raw_matrix: list[Any]) -> None:
        for line in raw_matrix:
            print(line, file=OUT)
