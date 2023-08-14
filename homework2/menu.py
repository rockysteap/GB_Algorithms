from service import header
def show_main():
    header(' Меню заданий ')
    print('''     0 <- Работа алгоритма пирамидальной сортировки. 
     1 <- Доработка алгоритма сортировки подсчетом. 
     2 <- Эксперименты с алгоритмами. 
     3 <- Имитация БД.''')
    header(' \'7\' -> выход ', 'right')


def user_input():
    typed = ''
    while typed not in ['0', '1', '2', '3', '7']:
        typed = input('> ')
    return int(typed)
