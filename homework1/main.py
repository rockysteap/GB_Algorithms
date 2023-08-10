import time
from dices import *

print(f"Всего {dice} кубиков с {n} сторонами.")
start = time.time()
throw(dice, s)
# print(f"Уникальные комбинации в отсортированном виде: {sorted(combos)}.")  # Распечатать комбинации
print(f"Количество уникальных комбинаций {len(combos)}.")
print(f"Время выполнения {time.time() - start} сек.")
