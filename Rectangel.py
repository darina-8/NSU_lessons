from dataclasses import dataclass


@dataclass
class Rectangle:
    w: int
    h: int

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return (self.w + self.h) * 2

    def __eq__(self, other):
        return self.area() == other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __add__(self, other):
        if self.w != other.w:
            raise ValueError("Ширина должна совпадать")
        return Rectangle(self.w, self.h + other.h)

    def __str__(self):
        return f'Прямоугольник: {self.w}*{self.h}'
