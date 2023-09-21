a : list[int] = [1,2,3,3,5]
b : list[int] = [0,0,1,0,1]

def mask_lisT(array: list[int], mask: list[int]) -> list[int]:
    return [val * mask[i] for i, val in enumerate(array)]

def test_mask_list():
    print('проверка')
    assert mask_lisT([1,2,3], [0,1,0]) == [0,2,0]
# for i, val in enumerate(a):
#     print(f'index = {i}')
#     print(f'value = {val}\n')