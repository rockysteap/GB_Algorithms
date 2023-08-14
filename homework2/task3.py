from random import randint
from time import time

from homework2.service import (advanced_list_gen, header, is_digits_list, running_time, print_digits_list_data_or_info,
                               print_symbolic_list_info)
from counting_sort import counting_sort
from quick_sort import quick_sort
from binary_search import binary_search


def task3():
    typed, query, original_lst, sorted_lst = '', int, [], []
    # Шаг 1 - генерируем случайный список.
    # Можно вывести на экран.
    header(' Генерация списка ')
    print(f'  1 <- Ввести параметры вручную.')
    header(' \'0\' -> автогенерация ', 'right')
    while typed not in ['1', '0']:
        typed = input('> ')
    match int(typed):
        case 1:
            original_lst = advanced_list_gen()
        case 0:
            original_lst = advanced_list_gen(query=False, lower_n=10_000, upper_n=20_000,
                                             lower_start=-2_000, lower_end=-1_000,
                                             upper_start=1_000, upper_end=2_000,
                                             symbols=randint(1, 3),  # 1->цифры, 2->буквы, 3->1+2+пунктуация
                                             word_min_len=randint(1, 4), word_max_len=randint(4, 20))
    input('Нажмите Enter для продолжения...')
    # Шаг 2 - ваша программа выбирает наилучший вариант сортировки исходя из параметров
    # входного массива - как минимум, из двух вариантов - из сортировки подсчетом и из быстрой сортировки.
    header(' Выбор алгоритма сортировки ')
    is_digit = is_digits_list(original_lst)
    if is_digit and max(original_lst) - min(original_lst) < len(original_lst) * 0.25:
        header(' Использована сортировка подсчетом ')
        print_digits_list_data_or_info(original_lst)
        sorted_lst = running_time(counting_sort, original_lst)
    else:
        header(' Использована быстрая сортировка ')
        print_digits_list_data_or_info(original_lst) if is_digit else print_symbolic_list_info(original_lst)
        sorted_lst = running_time(quick_sort, original_lst)
    # Шаг 3 - производится сортировка и создается некая коллекция данных, которая хранит в себе
    # первоначальное расположение элементов. Засекаем время выполнения и выводим на экран.
    header()
    input('Нажмите Enter для продолжения...')
    # Шаг 4 - вы вводите число с клавиатуры, далее выполняется бинарный поиск всех таких значений.
    # Засекаем время выполнения и выводим на экран.
    header(' Бинарный поиск ')
    if not is_digit:
        print(f' Бинарный поиск применить невозможно к символьному массиву')
        return
    print(f'  Введите число для поиска его индекса в списке')
    while True:
        try:
            user_input = input('> ')
            query = tuple(map(int, user_input.split()))[0]
        except ValueError:
            print('> Некорректный ввод ')
        else:
            break
    starting = time()
    res_lst = binary_search(sorted_lst, query)
    duration = time() - starting
    # Шаг 5 - вам выводятся индексы первоначального списка с шага 1, где находились такие числа.
    # Шаги 4-5 можно сделать внутри цикла while True.
    if res_lst:
        print(f'Число {query} найдено по индексам {sorted(res_lst)}')
        print(f'Обратная проверка. Запрос по индексам:')
        for c, i in enumerate(res_lst):
            print(f'{c + 1}. По индексу {i=} находится значение {sorted_lst[i]}. ')
    else:
        print(f'Число {query} в списке не найдено')
    print(f'Выполнение за {duration} сек.')
    header()
    input('Нажмите Enter для продолжения...')
