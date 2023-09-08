N = int(input())
def time(N):
    hours = N // 3600
    minute = N % 3600 // 60
    print(f'{hours} часов и {minute} минут')
time(N)