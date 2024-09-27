import math
print("Введите числа")
a, b, c = int(input()), int(input()), int(input())
def solve_quadratic_equation(a, b, c):
    # Рассчитаем дискриминант
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        # Два различных корня
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
    elif discriminant == 0:
        # Один корень (два одинаковых)
        x = -b / (2*a)
        return x
    else:
        # Дискриминант отрицателен, корней нет
        return None


eq1 = solve_quadratic_equation(a, b, c)
print(eq1)

