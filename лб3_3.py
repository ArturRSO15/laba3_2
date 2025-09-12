from abc import ABC, abstractmethod#импорт модуля для работы с абстрактными классами 
import math#импорт математического модуля для использования константы пи и функций sqrt


class Shape(ABC):#объявление абстрактного класса shape, наследующего от ABC
    @abstractmethod#декоратор для объявления абстрактного метода 
    def area(self): pass#абстрактный метод area()-должен быть реаллизован в дочерних классах 

    @abstractmethod
    def perimeter(self): pass#абстрактный метод perimetr()-также должен быть реализован 


class Rectangle(Shape):#класс прямоугольник, наследующий от абстрактного класса shape. Должен реализовать все абстрактные методы 
    def __init__(self, width, height):#конструктор класса rectangle принимает ширину и высоту 
        self.width = width# инициализация атрибута width(ширина)
        self.height = height#инициализация атрибута height(высота)

    def area(self): return self.width * self.height#реализация метода area() для прямоугольника площ=ширина * высота 

    def perimeter(self): return 2 * (self.width + self.height)#реализация метода perimetr() для прямоугольника 


class Circle(Shape): # класс круг наследующий от shape 
    def __init__(self, radius):# конструктор класса curcle принимает радиус 
        self.radius = radius#инициализация атрибута радиус radius

    def area(self): return math.pi * self.radius ** 2 # реализация метода area() для круга 

    def perimeter(self): return 2 * math.pi * self.radius#реализация метода perimetr() для круга (длинна окружности)


class Triangle(Shape): #класс треугольник, наследующий от shape 
    def __init__(self, a, b, c):# конструктор класса triangle принимает три стороны треугольника 
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self): return self.a + self.b + self.c # реализация метода perimetr() для треугольника 

    def area(self): #реализация метода area для треугольника(формула герона) 
        p = self.perimeter() / 2#вычисление полупериметра для формулы герона 
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))#формула герона для площади треугольника 


# Пример использования
shapes = [Rectangle(4, 5), Circle(3), Triangle(3, 4, 5)]
for shape in shapes:

    print(f"{type(shape).__name__}: Area = {shape.area():.2f}, Perimeter = {shape.perimeter():.2f}")
