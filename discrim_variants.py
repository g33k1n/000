elif discriminant == 0:
        # Один корень (два одинаковых)
        x = -b / (2*a)
        return x
    else:
        # Дискриминант отрицателен, корней нет
        return None
