# numbers: list = [
#     1, 2, 3, 4, 5, 6, 7, 8, 9
# ]

# for n in numbers:
#     if n % 3 == 0:
#             print(f'число кратно 3 - {n}')
#     else:
#         print(f'число не кратно 3 - {n}')


n = int(input())

# while n > 0:
#     print(n)
#     n -= 1

a = []
while n > 0:
    a.append(n)
    n -= 1
a.reverse()
print(a)    