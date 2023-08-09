from random import randint
import time


def perebor(x):
    start = time.time()
    for i in range(upper + 1):
        if i == x:
            break
    fin = time.time()
    print(f"Число отгадано и это {i} за {i} итераций")
    print(f"Времени ушло {fin - start}")
    print()


def random_guess(x):
    start = time.time()
    k = 1
    num = randint(0, upper)
    while x != num:
        num = randint(0, upper)
        k += 1
    fin = time.time()
    print(f"Число отгадано и это {num} за {k} итераций")
    print(f"Времени ушло {fin - start}")
    print()


def smart_random_guess(x):
    start = time.time()
    k = 1
    num = randint(0, upper)
    s = { num }
    while x != num:
        while num in s:
            num = randint(0, upper)
        s.add(num)
        k += 1
    fin = time.time()
    print(f"Число отгадано и это {num} за {k} итераций")
    print(f"Времени ушло {fin - start}")
    print()


def from_list(x):
    start = time.time()
    k = 0
    sp = [x for x in range(upper + 1)]
    a = None
    while a != x:
        index = randint(0, len(sp) - 1)
        a = sp.pop(index)
        k += 1
    fin = time.time()
    print(f"Число отгадано и это {a} за {k} итераций")
    print(f"Времени ушло {fin - start}")
    print()


def binary_search(x):
    start = time.time()
    k = 1
    left = 0
    right = upper
    current = round((right + left) / 2)
    while current != x:
        if current < x:
            left = current + 1
        else:
            right = current - 1
        current = round((right + left) / 2)
        k += 1
        # print(f"Left: {left} Right: {right} Current: {current} ")
        # input()
    fin = time.time()
    print(f"Число отгадано и это {current} за {k} итераций")
    print(f"Времени ушло {fin - start}")
    print()


upper = 100

x = randint(0, upper)

perebor(x)
random_guess(x)
# smart_random_guess(x)
from_list(x)
binary_search(x)


import time

0, 1, 1, 2, 3, 5 ,8, 13, 21

n = 20

def Iter_Fib(n):
    f1 = 0
    f2 = 1
    for i in range(n - 2):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
    if n > 2: return f2
    if n == 1: return 1
    if n == 0: return 0


def Fib_rec(numb1):
    if numb1 == 1: return 0
    if numb1 == 2: return 1
    return Fib_rec(numb1 - 1) + Fib_rec(numb1 - 2)


for i in range(10, 50, 10):
    start = time.time()
    print(f"{i=}")
    Fib_rec(i)
    print(time.time() - start)
    start = time.time()
    Iter_Fib(i)

    print(time.time() - start)