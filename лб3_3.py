from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self): return self.width * self.height

    def perimeter(self): return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self): return math.pi * self.radius ** 2

    def perimeter(self): return 2 * math.pi * self.radius


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self): return self.a + self.b + self.c

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


# Пример использования
shapes = [Rectangle(4, 5), Circle(3), Triangle(3, 4, 5)]
for shape in shapes:
    print(f"{type(shape).__name__}: Area = {shape.area():.2f}, Perimeter = {shape.perimeter():.2f}")