from service import header
from service import simple_list_gen
from service import running_time
from quick_sort import quick_sort
from heap_sort import heap_sort
from heap_sort_memo import heap_sort_memo

def task0():
    header(' Пирамидальная сортировка ')
    my_lst = simple_list_gen(-10_000, 10_000, 100_000)
    print(my_lst) if len(my_lst) <= 20 else print(f'Кол-во элементов {len(my_lst):,} '
                                                  f'от {min(my_lst):,} до {max(my_lst):,}')
    running_time(heap_sort, my_lst)
    print(my_lst) if len(my_lst) <= 20 else None

    header()
    print()
    header(' Теория о бинарных деревьях ')
    print(' 1 <- Посмотреть ')
    header(' \'7\' -> выход ', 'right')

    typed = ''
    while typed not in ['1', '7']:
        typed = input('> ')
        match typed:
            case '1':
                heap_sort_memo()
            case '7':
                break
