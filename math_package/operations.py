from decimal import Decimal

from math_package.matrix import Matrix
from math_package.configuration import ERR


class Operation:
    @staticmethod
    def check_diagonal_dominance(matrix: Matrix) -> bool:
        less_than_diagonal = 0
        less_or_equal_diagonal = 0
        for i in range(matrix.lines_count):
            diagonal_element = matrix.get_cell(i, i)
            line_sum = sum(matrix.get_line(i)) - diagonal_element
            if line_sum < diagonal_element:
                less_than_diagonal += 1
            if line_sum <= diagonal_element:
                less_or_equal_diagonal += 1

        if less_or_equal_diagonal == matrix.lines_count and less_than_diagonal >= 1:
            return True
        return False

    @staticmethod
    def get_max_from_diagonal_if_possible(line: list[Decimal], diagonal_index: int) -> tuple[int, Decimal]:
        """ Если в строке будет несколько одинаковых элементов (включая диагональный),
        являющихся максимальными, функция вернёт индекс диагонального элемента. В
        случае одного максимального элемента (или отсутствия максимума на диагональнали)
        будет возвращён первый попавшийся.

        :param line: строка матрицы
        :param diagonal_index: индекс диагонального элемента в текущей строке
        :return: кортеж, состоящий из индекса максимального элемента и самого элемента
        """
        max_element = max(line)
        max_element_duplicates = [i for i, x in enumerate(line) if x == max_element]
        if line.count(max_element) > 1 and diagonal_index in max_element_duplicates:
            return diagonal_index, max_element
        return max_element_duplicates[0], max_element

    @staticmethod
    def make_matrix_diagonally_dominantly(matrix: Matrix) -> Matrix | None:
        max_elements_positions = []
        for i in range(matrix.lines_count):
            index, max_element = Operation.get_max_from_diagonal_if_possible(matrix.get_line(i), i)
            max_elements_positions.append({"line_number": i, "max_elem_index": index, "max_elem": max_element})

        # Если матрицу можно привести к виду диагонального преобладания, не будет повторов индексов
        # максимальных элементов (все они будут находиться на различных позициях)
        if len(set([element["max_elem_index"] for element in max_elements_positions])) != matrix.lines_count:
            print("Ошибка! Не удалось привести к виду диагонального преобладания", file=ERR)
            return None

        result = [0] * matrix.lines_count
        for i in range(matrix.lines_count):
            current_element = max_elements_positions[i]
            result[current_element["max_elem_index"]] = matrix.get_line(current_element["line_number"])

        return Matrix(result)
