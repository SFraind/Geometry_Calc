import math

def circle_area(radius):
    if radius < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return math.pi * (radius ** 2)


def triangle_area(side1, side2, side3):
    if any(side <= 0 for side in [side1, side2, side3]):
        raise ValueError("Длины сторон должны быть положительными числами")

    # Проверка на возможность существования треугольника
    if side1 >= side2 + side3 or side2 >= side1 + side3 or side3 >= side1 + side2:
        raise ValueError("Это не может быть треугольник")

    s = (side1 + side2 + side3) / 2
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return area


def rectangle_area(length, width):
    if length < 0 or width < 0:
        raise ValueError("Длина и ширина не могут быть отрицательными")
    return length * width


def calculate_area(*args):
    if len(args) == 1:
        return circle_area(args[0])
    elif len(args) == 2:
        return rectangle_area(args[0], args[1])
    elif len(args) == 3:
        return triangle_area(*args)
    else:
        raise ValueError("Неизвестный тип фигуры")


def is_right_triangle(side1, side2, side3):
    sides = [side1, side2, side3]
    sides.sort()
    return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2
