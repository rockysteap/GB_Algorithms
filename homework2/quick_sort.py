# Быстрая сортировка

def quick_sort(lst):
    less = []
    equal = []
    greater = []
    if len(lst) > 1:
        pivot = lst[0]
        for x in lst:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return lst
