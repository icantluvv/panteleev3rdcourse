a = [] #создали массив
cnt = int(input()) #вводим кол-во элементов массива
b = 0 # счетчик
if (cnt >= 2): # проверка от дураков, программа работает, только если кол-во элементов массива >=2 
    
    while b < cnt:
        n = int(input("введите элементы массива: "))  #вводим элементы массива
        a.append(n) #добавляем в список
        b += 1 #наращиваем счетчик
    print(f"ваш массив: {a}")  #печатаем массив

    otvet = [] #создали массив для индексов
    for i in range(len(a)-1): #перебираем массив и сверяем соседние эллементы
        if (a[i] - a[i+1] < -1): #если нынешний минус следующий меньше -1, т.е некст число больше на 2:
            otvet.append(i+1) #то заносим индекс в массив
    if (len(otvet) == 0): #проверка если индексов таких нет
        print("Не найдено")
    else: print(f"ответ (индекс числа(ел), большего(их) предыдущего(их) на 2): {otvet}") # и выводим массив

else:(print("количество элементов массива по условию больше 2 (это проверка от дураков, не будьте дураком)"))