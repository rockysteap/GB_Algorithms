from service import header
import menu
from task0 import task0
from task1 import task1
from task2 import task2
from task3 import task3


def main():
    while True:
        menu.show_main()
        typed = menu.user_input()
        match typed:
            case 0:
                task0()
            case 1:
                task1()
            case 2:
                task2()
            case 3:
                task3()
            case 7:
                header(' Программа завершена ')
                break


if __name__ == '__main__':
    main()
