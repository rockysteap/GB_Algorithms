# Пирамидальная сортировка (Сортировка кучей)
def heap_sort(lst):
    heap_size = len(lst)
    build_max_heap(lst, heap_size)
    for i in range(heap_size - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify_max(lst, i, 0)


def build_max_heap(lst, heap_size):
    for i in range(heap_size, -1, -1):
        heapify_max(lst, heap_size, i)


def heapify_max(lst, heap_size, i):
    max_i = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < heap_size and lst[i] < lst[left]:
        max_i = left
    if right < heap_size and lst[max_i] < lst[right]:
        max_i = right
    if max_i != i:
        lst[i], lst[max_i] = lst[max_i], lst[i]
        heapify_max(lst, heap_size, max_i)
