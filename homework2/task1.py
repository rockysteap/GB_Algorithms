from service import header
from service import simple_list_gen
from service import running_time
from counting_sort import counting_sort

def task1():
    header(' Сортировка подсчетом ')
    print(f'Работа с отрицательными значениями:')
    my_lst = simple_list_gen(-1000, 1000, 10_000)
    print(my_lst) if len(my_lst) <= 20 else print(f'Кол-во элементов {len(my_lst):,} '
                                                  f'от {min(my_lst):,} до {max(my_lst):,}')
    sorted_list = running_time(counting_sort, my_lst)
    print(sorted_list) if len(sorted_list) <= 20 else None

    header()
    input('Нажмите Enter для продолжения...')
