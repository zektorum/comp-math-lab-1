from typing import Any

from math_package.exception import EmptyMatrixCreationException


class Matrix:
    def __init__(self, raw_data: list[Any]):
        self.data = raw_data
        if not raw_data:
            raise EmptyMatrixCreationException
        self.rows_count = len(self.data[0])
        self.lines_count = len(self.data)

    def get_cell(self, i: int, j: int):
        return self.data[i][j]

    def get_line(self, n: int) -> list[Any]:
        try:
            line = self.data[n]
            return line
        except IndexError:
            return []

    def get_row(self, n: int) -> list[Any]:
        try:
            pass
        except IndexError:
            pass

    def swap_lines(self, a: int, b: int) -> None:
        self.data[a], self.data[b] = self.data[b], self.data[a]

    def __str__(self):
        out = ""
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                out += str(self.data[i][j]) + " "
            out += "\n"
        return out
