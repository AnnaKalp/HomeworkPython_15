#Создайте класс Матрица. Добавьте методы для:
#- вывода на печать
#- сравнения
#- сложения
#- умножения матриц

# Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.
import logging
import argparse

logging.basicConfig(filename='Log/log_10.log',
                    filemode='a',
                    encoding='utf-8',
                    format='{levelname:<6} - {asctime} в модуле {module} функция "{funcName}()" : {msg}',
                    style='{',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


class MatrixExeption(Exception):

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return f'Конфликт размерности матриц, matrix_a = {self.x1}x{self.y1}; matrix_b = {self.x2}x{self.y2}'


class Matrix():
    '''Класс для создания матриц и операциями + и * над ними'''

    def __init__(self, matrix: list):
        self._matrix = matrix

    def __eq__(self, other: object) -> bool:
        '''Cравнение 2 матриц между собой, равны, если: равны размерности и строки\столбцы содержат одинаковые элементы'''

        if len(self._matrix) != len(other._matrix):
            return False
        else:
            __flag = False
            for i in range(len(self._matrix)):
                if self._matrix[i] == other._matrix[i]:
                    __flag = True
                else:
                    self._flag = False
            return __flag

    def __add__(self, other):
        '''Сложение матриц одинаковой размерности'''

        if len(self._matrix) != len(other._matrix):
            logger.error(MatrixExeption(len(self._matrix), len(self._matrix[0]), len(other._matrix), len(other._matrix[0])))
        else:
            result_matrix = []
            for i in range(len(self._matrix)):
                line1 = self._matrix[i]
                line2 = other._matrix[i]
                c = [x + y for x, y in zip(line1, line2)]
                result_matrix.append(c)
            return Matrix(result_matrix)

    def __mul__(self, other):
        '''Перемножение матриц'''

        if len(self._matrix[0]) != len(other._matrix):
            logger.error(MatrixExeption(len(self._matrix), len(self._matrix[0]), len(other._matrix), len(other._matrix[0])))
        else:
            result_matrix = []
            for i in range(len(self._matrix)):
                new_row = []
                for j in range(len(other._matrix[0])):
                    elem = 0
                    for k in range(len(other._matrix)):
                        elem += self._matrix[i][k] * other._matrix[k][j]
                    new_row.append(elem)
                result_matrix.append(new_row)
            return Matrix(result_matrix)

    def __str__(self) -> str:
        result_string = ''

        for i in self._matrix:
            result_string += f'{i}\n'

        return result_string


if __name__== '__main__':

    parser = argparse.ArgumentParser(description="Принимаем строку с данными")
    parser.add_argument('-matrix_1', type=str, default="[[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
    parser.add_argument('-matrix_2', type=str, default="[[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
    parser.add_argument('-matrix_3', type=str, default="[[10, 2, 3], [40, 5, 6], [7, 8, 90]]")
    parser.add_argument('-matrix_4', type=str, default="[[10, 2, 3], [40, 5, 6]]")

    args = parser.parse_args()

    try:
        matrix_1 = [[int(j) for j in i] for i in eval(args.matrix_1)]
    except ValueError as e:
        logger.error(f'Переданные данные: матрица matrix_1 = {args.matrix_1}, {e}')
        matrix_1 = [[-1]]

    try:
        matrix_2 = [[int(j) for j in i] for i in eval(args.matrix_2)]
    except ValueError as e:
        logger.error(f'Переданные данные: матрица matrix_2 = {args.matrix_2}, {e}')
        matrix_2 = [[-1]]

    try:
        matrix_3 = [[int(j) for j in i] for i in eval(args.matrix_3)]
    except ValueError as e:
        logger.error(f'Переданные данные: матрица matrix_1 = {args.matrix_3}, {e}')
        matrix_3 = [[-1]]

    try:
        matrix_4 = [[int(j) for j in i] for i in eval(args.matrix_4)]
    except ValueError as e:
        logger.error(f'Переданные данные: матрица matrix_1 = {args.matrix_4}, {e}')
        matrix_4 = [[-1]]

    matrix_1 = Matrix(matrix_1)
    matrix_2 = Matrix(matrix_2)
    matrix_3 = Matrix(matrix_3)
    matrix_4 = Matrix(matrix_4)

    #Cравнение матриц
    logger.info(matrix_1 == matrix_2)
    logger.info(matrix_1 == matrix_3)

    # Сложение матриц
    logger.info(matrix_1 + matrix_3)
    logger.info(matrix_1 + matrix_4)

    # Умножение матриц
    logger.info(matrix_1 * matrix_3)
    logger.info(matrix_1 * matrix_4)
