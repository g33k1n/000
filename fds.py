#Исправлена формула вычисления корней через дискриминант
if discriminant > 0:
        # Два различных корня
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
