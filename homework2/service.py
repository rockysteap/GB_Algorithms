import string
from random import randint, choice
from time import time


# Генератор списка простой
def simple_list_gen(min_value=-5, max_value=5, lst_len=10):
    return [randint(min_value, max_value) for _ in range(lst_len)]


# Генератор списка продвинутый
def advanced_list_gen(query=False, lower_n=20, upper_n=20,
                      lower_start=-200, lower_end=-100, upper_start=100, upper_end=200,
                      symbols=1, word_min_len=1, word_max_len=14):
    if query:
        user_data = advanced_list_user_query()  # метод-опросник
        (lower_n, upper_n, lower_start, lower_end, upper_start, upper_end, symbols, word_min_len, word_max_len) = \
            [i for i in user_data]
    n = randint(lower_n, upper_n)  # кол-во элементов
    match symbols:
        case 1:
            lower = randint(lower_start, lower_end)  # нижняя граница элементов
            upper = randint(upper_start, upper_end)  # верхняя граница элементов
            print_list_data(lower, upper, n, symbols, word_min_len, word_max_len)
            return [randint(lower, upper) for _ in range(n)]
        case 2 | 3:
            symbols_set = string.ascii_letters if symbols == 2 else string.ascii_letters + string.punctuation
            print_list_data(0, 0, n, symbols, word_min_len, word_max_len)
            return [''.join(choice(symbols_set) for _ in range(randint(word_min_len, word_max_len))) for __ in range(n)]


# Печать списка сразу после генерации
def print_list_data(lower, upper, n, symbols, word_min_len, word_max_len):
    header(' Сгенерирован список ')
    print(f'  Использованы следующие символы:')
    print(f'  {string.digits}') if symbols in [1, 3] else None
    print(f'  {string.ascii_letters}') if symbols in [2, 3] else None
    print(f'  {string.punctuation}') if symbols in [3] else None
    header(' Параметры генерации ')
    print(f'  Нижний диапазон: {lower:,}, верхний диапазон: {upper:,}') if symbols in [1] else None
    print(f'  Количество элементов каждого слова от {word_min_len} до {word_max_len}') if symbols in [2, 3] else None
    print(f'  Всего элементов {n:,}')
    header()


# Вспомогательный метод продвинутого генератора для запроса данных в случае выбора ручного ввода
def advanced_list_user_query(lower_n=20, upper_n=20,
                             lower_start=-200, lower_end=-100, upper_start=100, upper_end=200):
    symbols, word_min_len, word_max_len, typed = int, int, int, ''
    header(' Генератор списка ')
    print(f'  В генерацию элементов списка войдут следующие символы:\n'
          f'  1 <- Цифры.\n'
          f'  2 <- Буквы английского алфавита (прописные и строчные).\n'
          f'  3 <- Цифры, буквы и знаки пунктуации.')
    header()
    while typed not in ['1', '2', '3']:
        typed = input('> ')
    match int(typed):
        case 1:
            symbols = 1
            header(' Задайте границы для генерации элементов списка ')
            print(f'  Введите в одной строке четыре числа:\n'
                  f'  шаблон -> [мин] [макс] [мин] [макс]\n'
                  f'     для нижней границы и верхней границы')
            header(' \'0\' -> по умолчанию ', 'right')
            while True:
                try:
                    user_input = input('Введите через пробел > ')
                    if user_input == '0':
                        break
                    typed = tuple(map(int, user_input.split()))
                    lower_start, lower_end, upper_start, upper_end = [i for i in typed]
                except ValueError:
                    print('> Некорректный ввод ')
                else:
                    break
        case 2 | 3:
            symbols = 2 if typed == '2' else 3
            header(' Задайте мин и макс длину слова ')
            print(f'  Параметры по умолчанию 1 и 14 (макс -> 20 символов)')
            header(' \'0\' -> по умолчанию ', 'right')
            while True:
                try:
                    user_input = input('Введите через пробел > ')
                    if user_input == '0':
                        word_min_len = 1
                        word_max_len = 14
                        break
                    typed = tuple(map(int, user_input.split()))
                    word_min_len = typed[0] if typed[0] in range(1, 20) else 1
                    word_max_len = typed[1] if typed[1] in range(1, 21) else 14
                except ValueError:
                    print('> Некорректный ввод ')
                else:
                    break
    header(' Задайте границы для генерации кол-ва элементов ')
    print(f'  Введите в одной строке два числа:\n'
          f'  шаблон -> [мин] [макс]')
    header(' \'0\' -> по умолчанию ', 'right')
    while True:
        try:
            user_input = input('Введите через пробел > ')
            if user_input == '0':
                break
            typed = tuple(map(int, user_input.split()))
            lower_n, upper_n = [i for i in typed]
        except ValueError:
            print('> Некорректный ввод ')
        else:
            break
    return lower_n, upper_n, lower_start, lower_end, upper_start, upper_end, symbols, word_min_len, word_max_len


# Текстовый разделитель
def header(message='', align='center', line_len=60):
    match align:
        case 'center':
            part_line = int(line_len - len(message)) // 2 if int(line_len - len(message)) // 2 > 0 else 0
            print(f"{'-' * part_line}{message}{'-' * part_line}")
        case 'left':
            part_line_left = 4 if line_len - len(message) - 4 > 0 else 0
            part_line_right = line_len - len(message) - 4 if line_len - len(message) - 4 > 0 else 0
            print(f"{'-' * part_line_left}{message}{'-' * part_line_right}")
        case 'right':
            part_line_left = line_len - len(message) - 4 if line_len - len(message) - 4 > 0 else 0
            part_line_right = 4 if line_len - len(message) - 4 > 0 else 0
            print(f"{'-' * part_line_left}{message}{'-' * part_line_right}")


# Определить тип элементов списка (цифровой?)
def is_digits_list(lst):
    for i in lst:
        try:
            int(i)
        except ValueError:
            return False
    return True


# Печать инфо списка из цифровых элементов с условием размерности
def print_digits_list_data_or_info(lst, print_data=True, max_size_to_show=20):
    print(lst) if len(lst) <= max_size_to_show \
        else print(f'Кол-во элементов {len(lst):,} от {min(lst):,} до {max(lst):,}') \
        if print_data \
        else print(lst) if len(lst) <= max_size_to_show else None


# Печать инфо списка из символьных элементов
def print_symbolic_list_info(lst):
    min_len, max_len = len(lst[0]), len(lst[0])
    for i in range(1, len(lst) - 1):
        if len(lst[i]) > max_len:
            max_len = len(lst[i])
        if len(lst[i]) < min_len:
            min_len = len(lst[i])
    print(f'Кол-во элементов {len(lst):,} длиной от {min_len} до {max_len}')


# Замер временных рамок
def running_time(func, x):
    starting = time()
    returned_value = func(x)
    duration = time() - starting
    print(f'Выполнение за {duration} сек.')
    if returned_value is not None:
        return returned_value
