# num = int(input())

# def guess(num: int) -> int | str:
#     if num > 0:
#         a = 0
#         for i in range (1, num + 1):
#             if i*i == num:
#                 a += 1
#                 print(i)
#         if a == 0 : print('ne mogu') 
#     else: print('ne mogu')
# guess(num)

def guess(num: int) -> int | str:
    if num <= 0:
        print("введите норм число")
    for i in range(1, num+1):
        if i**2 == num:
            return i
        else:
            i = i + 1
        if i not in range (1, num + 1):
            return "я так не могу"

num = int(input('Введите целое натуральное число: '))
print(guess(num))
