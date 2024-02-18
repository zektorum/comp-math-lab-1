from abc import ABC, abstractmethod
from enum import Enum

from math_package.configuration import ERR, OUT
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

    def process_raw_matrix(self, raw_matrix: list[str]) -> Matrix:
        pass

    def read(self, input_type: InputType) -> Matrix:
        raw_matrix = self.read_raw_matrix()
        return self.process_raw_matrix(raw_matrix)


class RawMatrixReader(ABC):
    @abstractmethod
    def read(self) -> list[str]:
        pass


class MatrixReaderFromFile(RawMatrixReader):
    def read(self) -> list[str]:
        """ Возвращает считанную с клавиатуры матрицу в виде массива строк.

        :return: список состоящий из строк матрицы
        """
        print("Введите имя файла: ", file=OUT)
        filename = input()

        try:
            with open(filename, "r") as file:
                lines = file.readlines()
                if lines is not bytes:
                    return lines
                print("Ошибка! Из файла считаны байтовые строки", file=ERR)
                return []
        except FileNotFoundError:
            print("Ошибка! Файл не найдет", file=ERR)
            return []


class MatrixReaderFromKeyboard(RawMatrixReader):
    def read(self) -> list[str]:
        hint = "Введите количество %s:"
        while True:
            try:
                print(hint.format("строк"), file=OUT)
                rows = int(input())

            except ValueError:
                print("")
