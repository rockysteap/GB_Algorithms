"""Необходимо написать алгоритм поиска всех доступных комбинаций
(посчитать количество) для количества кубиков K с количеством граней N """

dice = 7  # k - кол-во кубиков
n = 6  # n - кол-во граней
s = str()
combos = set()

def throw(k: int, output: str):
    if k == 1:
        for i in range(1, n + 1):
            combos.add(int(''.join(sorted(output + str(i)))))
    else:
        for i in range(1, n + 1):
            throw(k - 1, output + str(i))
