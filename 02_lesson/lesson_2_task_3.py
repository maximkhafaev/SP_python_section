import math

def square(side):
    return math.ceil(side*side)

side = float(input('Введите длину стороны: '))
print(square(side))