"""Треугольник существует только тогда, когда сумма
любых двух его сторон больше третьей. Дано a, b, c -
стороны предполагаемого треугольника. Требуется сравнить
длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух
других, то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним,
равнобедренным или равносторонним."""

# Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.

import logging
import argparse

logging.basicConfig(filename='Log/log_1.log',
                    filemode='a',
                    encoding='utf-8',
                    format='{levelname:<6} - {asctime} в модуле {module} функция "{funcName}()" : {msg}',
                    style='{',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


class TriangleException(Exception):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Треугольник со сторонами {self.a}, {self.b}, {self.c} не может существовать'


if __name__=="__main__":

    parser = argparse.ArgumentParser(description="Принимаем строку с данными")
    parser.add_argument('-a', type=str, default='4')
    parser.add_argument('-b', type=str, default='4')
    parser.add_argument('-c', type=str, default='5')

    args = parser.parse_args()

    try:
        a = int(args.a)
    except ValueError as e:
        logger.error(f'Переданные данные: сторона a = {args.a}, {e}')
        a = -1

    try:
        b = int(args.b)
    except ValueError as e:
        logger.error(f'Переданные данные: сторона b = {args.b}, {e}')
        b = -1

    try:
        c = int(args.c)
    except ValueError as e:
        logger.error(f'Переданные данные: сторона c = {args.c}, {e}')
        c = -1


    if a + b <= c or a + c <= b or b + c <= a:
        logger.error(TriangleException(a, b, c))
    else:
        if a == b == c:
            logger.info("Треугольник является равносторонним.")
        elif a == b or a == c or b == c:
            logger.info("Треугольник является равнобедренным.")
        else:
            logger.info("Треугольник является разносторонним.")