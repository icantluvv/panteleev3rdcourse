N = int(input()) #вводим
a = [] #массив
for i in range (N*(-1), N + 1): #проходимся от -N до N
    a.append(i**2) # в квадрат и закидываем в массив
print(a)