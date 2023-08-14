# Сортировка подсчетом
""" Включая отрицательные значения """

def counting_sort(in_lst):
    min_item = min(in_lst)
    max_item = max(in_lst)
    if min_item < 0:
        lst = [0 for _ in range(abs(min_item) + max_item + 1)]
    else:
        lst = [0 for _ in range(max_item + 1)]
    for i in in_lst:
        lst[i + abs(min_item)] = lst[i + abs(min_item)] + 1
    sorted_lst = []
    for i in range(len(lst)):
        if lst[i]:
            sorted_lst.extend([i - abs(min_item)] * lst[i])
    return sorted_lst
