a = input().split()
for i in range(0, len(a)):
    a[i] = int(a[i])
print(f'ваш массив: {a}')

otvet = []
for i in range(0, len(a)-1): 
    if (a[i] - a[i+1] < -1): 
        otvet.append(i+1) 
if (len(otvet) == 0): 
            print("Не найдено")
else: print(f"ответ: (индекс числа(ел), большего(их) предыдущего(их) на 2): {otvet}") # и выводим массив