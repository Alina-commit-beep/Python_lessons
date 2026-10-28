import math


def square(side):
    return math.ceil(side * side)


print(square(4))    # 16
print(square(2.5))  # 7  (6.25 округлили вверх)
print(square(3.1))  # 10 (9.61 округлили вверх)
