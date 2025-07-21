import math


def squar(side):
    return math.ceil(side * side)


num_side = int(input("Введите значение стороны квадрата: "))
print(f"Площадь квадрата: {squar(num_side)}")
