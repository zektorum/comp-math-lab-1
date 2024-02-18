from typing import Any


class Matrix:
    def __init__(self, raw_data: list[Any]):
        self.data = raw_data

    def get_line(self, n: int) -> list[Any]:
        try:
            line = self.data[n]
            return line
        except IndexError:
            return []

    def __str__(self):
        out = ""
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                out += str(self.data[i][j]) + " "
            out += "\n"
        return out
