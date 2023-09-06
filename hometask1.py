def task(n):
    sum_3 = 3 * (n // 3 * (n // 3 + 1) // 2)
    sum_5 = 5 * (n // 5 * (n // 5 + 1) // 2)
    sum_15 = 15 * (n // 15 * (n // 15 + 1) // 2)
    return sum_3 + sum_5 - sum_15

n = int(input("Введите n: "))
result = task(n)
print(f"Сумма чисел от 1 до {n}, делящихся на 3 или 5: {result}")
