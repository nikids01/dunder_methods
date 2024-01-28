from __future__ import annotations


class Point:
    def __init__(self, x: int, y: int) -> None:
        """Магический метод"""
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """Магический метод"""
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        """Магический метод"""
        return f"({self.x}, {self.y})"

    def __add__(self, another_point: Point) -> str:
        result_x = self.x + another_point.x
        result_y = self.y + another_point.y
        return f"({result_x}, {result_y})"

    def __sub__(self, another_point: Point) -> Point:
        result_x = self.x - another_point.x
        result_y = self.y - another_point.y
        return Point(result_x, result_y)

    def __eq__(self, another_point: Point) -> bool:
        """Если (x1 равен x2) и (y1 равен y2), вернет True, иначе False"""
        return self.x == another_point.x and self.y == another_point.y


# p1 = Point(5, 0)
# p2 = Point(10, 15)
# p4 = Point(5, 0)

# p3 = p1 - p2
# print(p3)

# print(p1 == p4)


class ComplexNumber:
    def __init__(self) -> None:
        """Создает 2 аттрибута real: int, img: int"""

    def __add__(self, cx: ComplexNumber) -> ComplexNumber:
        """Реальная часть складывается с реальной, воображаемая с воображаемой"""
        return

    def __sub__(self, cx: ComplexNumber) -> ComplexNumber:
        """Реальная часть отнимается с реальной, воображаемая с воображаемой"""
        return

    def __repr__(self) -> str:
        """Возвращает в формате: 5 + 7j"""
        return

    def __iadd__(self, cx: ComplexNumber) -> ComplexNumber:
        return

    def __isub__(self, cx: ComplexNumber) -> ComplexNumber:
        return

    def __eq__(self, cx: ComplexNumber) -> bool:
        return


# __add__ +
# __sub__ -
# __iadd__ +=
# __isub__ -=
# __eq__ ==
