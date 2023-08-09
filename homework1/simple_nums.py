"""ДЗ по желанию - найти все простые числа от 1 до N, где N вводится пользователем.
   Реализовать три различных алгоритма, включая решето Эратосфена.
   Оценить эффективность каждого подхода."""

import time

# пример алгоритма из лекции
def find_simple_numbers1(n: int) -> list:
    start = time.time()
    counter = 0
    result = list()
    for i in range(1, n):
        simple = True
        for j in range(2, i):
            counter += 1
            if i % j == 0:
                simple = False
        if simple:
            result.append(i)
    print("Algorithm 1: ", time.time() - start)
    print(f"{counter}: iteration(s) for {n}")
    return result

# пример алгоритма с хабра
def find_simple_numbers2(n):
    start = time.time()
    counter = 0
    lst = [2]
    for i in range(3, n, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            counter += 1
            if j * j - 1 > i:
                lst.append(i)
                break
            if i % j == 0:
                break
        else:
            lst.append(i)
    print("Algorithm 2: ", time.time() - start)
    print(f"{counter} iteration(s) for {n}")
    return lst

# решето Эратосфена 1 вариант
def sieve1(n):
    start = time.time()
    counter = 0
    sieve = set(range(2, n + 1))
    while sieve:
        counter += 1
        prime = min(sieve)
        sieve -= set(range(prime, n + 1, prime))
    print("Algorithm 3: ", time.time() - start)
    print(f"{counter} iteration(s) for {n}")

# решето Эратосфена 2 вариант
def sieve2(n):
    start = time.time()
    s = range(3, n + 1, 2)
    r = set(s)
    [r.difference_update(range(n << 1, s[-1] + 1, n)) for n in s if n in r]
    print("Algorithm 4: ", time.time() - start)
    print(f"____ iteration(s) for {n}")
    return r.union([2])

max = 10000
find_simple_numbers1(max)
find_simple_numbers2(max)
sieve1(max)
sieve2(max)
