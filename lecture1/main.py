def find_all_dividers(num: int) -> list:
    counter: int = 0
    result: list = list()
    for i in range(1, num):
        counter += 1
        if num % i == 0:
            result.append(i)
    print(f"{i} iteration(s) for {num}")
    return result


def find_simple_numbers(max: int) -> list:
    counter: int = 0
    result: list = list()
    for i in range(1, max):
        simple: bool = True
        for j in range(2, i):
            counter += 1
            if i % j == 0:
                simple = False
        if simple:
            result.append(i)
    print(f"{i} iteration(s) for {max}")
    return result


def fib(pos: int):
    if pos in [1, 2]:
        return 1
    return fib(pos - 1) + fib(pos - 2)


print(find_all_dividers(100))
print(find_simple_numbers(100))
print(fib(10))
