def convert_ab_to_int(a: str,b: str) -> tuple[int, int]:
    a,b = int(a), int(b)
    return(a,b)

 
while True:
    a,b = input('введи 2 числа ').split()
    try:
        a,b = convert_ab_to_int(a,b)
    except Exception as e:
        print(f'ошибка :{e}')
        print("введи числа!")
        print()
        continue

    ab_sum = a + b
    print(f'{a} + {b} = {ab_sum}')