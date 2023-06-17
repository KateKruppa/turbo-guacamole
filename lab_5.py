
from abc import ABC, abstractmethod
import math
from shapely.geometry import Polygon
from shapely import area as one_area, length as two_length


class Figure(ABC):

    @property
    @abstractmethod
    def area(self):
        return one_area(Polygon(self._coordinates))
    # вычисляет площадь многоугольника по координатам

    @property
    @abstractmethod
    def perimeter(self):
        return two_length(Polygon(self._coordinates))
    # вычисляет периметр многоугольника по координатам


class Triangle(Figure):
    def __init__(self, coordinates):
        if len(coordinates) != 3:
            raise FigureExceptions("треугольник должен иметь три координаты")
    # конструктор который принимет три координаты треугольника
    # если координат не три, во выводит предупреждение
        for i in coordinates:
            if len(i) != 2 or any(z < 0 for z in i):
                raise FigureExceptions("координаты могут иметь только положительные значения")
    # если есть отрицательные координаты, то выводит предупреждение

        self._coordinates = coordinates
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        x3, y3 = coordinates[2]
        self.a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        self.b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
        self.c = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
        if not (self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a):
            raise TriangleExceptions("треугольник не может существовать")
        # вычисление сторон треугольника и проверка на условие существования
        # если условие не выполняется, то выводится предупреждение

    @property
    def area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    # вычисление площади треугольника по формуле Герона

#    @property
#    def perimeter(self):
#        return self.a + self.b + self.c

    def view(self):
        if self.a == self.b or self.a == self.c or self.b == self.c:
            return 'Равнобедренный треугольник'
        elif self.a == self.b == self.c:
            return 'Равносторонний треугольник'
        else:
            return 'Разносторонний треугольник'
    # определение вида треугольна по признакам


def intersection (self, other):
    actual = Polygon(self._coordinates)
    another = Polygon(other._coordinates)
    return actual.intersects(another)
# проверка пересечения текущего треугольника с другим с помощью Polygon


class Quadrilateral(Figure):
    def __init__(self, coordinates):
        if len(coordinates) != 4:
            raise FigureExceptions("четырехугольник должен иметь четыре координаты")
        # конструктор который принимет четыре координаты четырехугольника
        # если координат не четыре, во выводит предупреждение

        for i in coordinates:
            if len(i) != 2 or any(z < 0 for z in i):
                raise FigureExceptions("координаты могут иметь только положительные значения")
        # если есть отрицательные координаты, то выводит предупреждение

        self._coordinates = coordinates
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        x3, y3 = coordinates[2]
        x4, y4 = coordinates[3]
        self.a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        self.b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
        self.c = math.sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
        self.d = math.sqrt((x1 - x4) ** 2 + (y1 - y4) ** 2)
        # вычисление длин сторон четырехугольника

        glo = Polygon(self._coordinates)
        if not glo.is_valid:
            raise QuadrilateralExceptions("четырехугольник не может существовать")
        # проверка на возможность существования четурехугольника

    @property
    def area(self):
        glo = Polygon(self._coordinates)
        return round(one_area(glo), 3)
    # вычисление площади с помощью one_area

    @property
    def perimeter(self):
        glo = Polygon(self._coordinates)
        return round(two_length(glo), 3)
    # вычисление периметра с помощью two_length

    def sings(self):
        diagonal1 = math.sqrt(self.a ** 2 + self.b ** 2)
        diagonal2 = math.sqrt(self.c ** 2 + self.d ** 2)
        # вычисление диагоналей
        if self.a == self.b and self.b == self.c and self.c == self.d:
            return 'Ромб'
        if self.a == self.c and self.b == self.d:
            return 'Параллелограмм'
        if self.a == self.c and self.b == self.d and diagonal1 == diagonal2:
            return 'Прямоугольник'
        else:
            return 'Произвольный четырехугольник'
        # определение вида четырехугольна по признакам

class FigureExceptions(Exception):
    pass


class TriangleExceptions(FigureExceptions):
    pass


class QuadrilateralExceptions(FigureExceptions):
    pass

# исключения для фигур

### помогали мне всем селом решить это..., спасибо Насте и Кириллу