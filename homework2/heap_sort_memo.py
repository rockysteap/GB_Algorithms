# Немного рассуждений и псевдокод (для понимания)
# для вывода на печать ветка '\' записана как '\\'
from homework2.service import header


def heap_sort_memo():
    header(' Двоичные (бинарные) деревья ')

    print("""
Структура, используемая в пирамидальной сортировке называется двоичная куча.
Двоичная куча — это законченное двоичное дерево, в котором элементы хранятся 
в особом порядке: значение в родительском узле больше (или меньше) значений 
в его двух дочерних узлах. Первый вариант называется max-heap, а второй — 
min-heap. Куча может быть представлена двоичным деревом или массивом.
Представление на основе массива является эффективным с точки зрения расхода 
памяти. Если родительский узел хранится в индексе i, левый дочерний элемент 
может быть вычислен как 2i + 1, а правый дочерний элемент — как 2i + 2 
(при условии, что индексирование начинается с 0).""")
    print("""
Максимальная куча -> когда родитель старше или равен потомкам.
Минимальная куча -> когда родитель младше или равен потомкам.
    """)
    header(' Теория сортировки ')
    print("""
Список(массив) представим в виде кучи (бинарное дерево).
Для сортировки приведём кучу к максимальной -> max_heap.
""")
    input('Нажмите Enter для продолжения...')
    print("""Возьмем array = [7,8,11,2,0,3,8,4,5,15]
и представим его в качестве бинарного дерева следующего вида:
индекс верхнего элемента равен 1 (для удобства начинаем с первого, а не с нулевого),
второго уровня 2 и 3 (это потомки родителя под индексом 1),
третьего уровня 4, 5, 6, 7 (4 и 5 потомки родителя 2, 6 и 7 потомки родителя 3) и так далее.

           7            <- элемент и его индекс ->              1
        /     \\                                              /     \\
       8       11       <- элемент и его индекс ->          2       3
     /   \\    /  \\                                        /   \\    /  \\
    2     0  3    8     <- элемент и его индекс ->       4     5  6    7
   / \\   /                                              / \\   /
  4   5 15              <- элемент и его индекс ->     8   9 10
  """)
    input('Нажмите Enter для продолжения...')
    print("""Формулы расчета индексов:
возьмем индекс родителя за i, тогда индекс левого потомка 2*i, правого 2*i+1;
чтобы найти родителя элемента, необходимо взять целочисленное деление 
на 2 от индекса потомка -> i // 2
(потомки с индексом 6 и 7 имеют родителя с индексом 6//2 и 7//2 или 3).

Расчет листьев (конечных элементов, не имеющих потомков):
leaves = A[floor(n/2) + 1] to A[n], где A - наш массив, n - его длина.
""")
    input('Нажмите Enter для продолжения...')
    print("""Тогда в нашем случае листья это элементы от A[floor(10/2) + 1] или A[6] до A[10],
иными словами элементы с индексами 6,7,8,9,10 -> листья.
Таким образом, элемент A[floor(10/2)] или A[5] -> крайний (самый нижний, самый правый) родитель,
который образует локальную кучу, в данном случае с одним потомком под индексом 10.

То есть за стартовый индекс в алгоритм передадим индекс -> len(list) // 2.
С него и начнем алгоритм сравнения и приведения нашей кучи к максимальной и
пройдем до первого элемента.

Смотрим на кучу с родительским индексом 5 и значением 0, в данной куче один потомок со значением 15.
Сравниваем значения, потомок больше родителя -> меняем значения.
   i = 5                                                      i = 4
           7          Дальше идем к локальной куче                     7
        /     \\       под родительским индексом 4,                  /     \\
       8       11     сравниваем значения, сначала                 8       11
     /   \\    /  \\    левого потомка, если оно больше           /   \\    /  \\
    2     15 3    8   родителя, записываем в max, затем        5    15  3    8
   / \\   /            правого потомка, если оно больше        / \\   /
  4   5 0             max, меняем местами с родителем.       4   2 0

Далее кучи с родительскими индексами
 ->          i = 3                        i = 2                        i = 1
       11 больше 3 или 8     |    5 < 15 -> не меняем    |       15 > 7 -> max=15
       ничего не меняется    |      15 > 8 -> меняем     |     11 < max -> меняем max и 7
                             |                           |
                 7           |              7            |              15
              /     \\        |           /     \\         |            /    \\
             8       11      |          15      11       |           7      11
           /   \\    /  \\     |        /   \\    /  \\      |         /   \\   /  \\
          5     15 3    8    |       5     8  3    8     |        5     8 3    8
         / \\   /             |      / \\   /              |       / \\   /
        4   2 0              |     4   2 0               |      4   2 0
    """)
    input('Нажмите Enter для продолжения...')
    print("""При прохождении по алгоритму создания максимальной кучи могут быть моменты,
когда меняя местами элементы локальной кучи, мы нарушаем правило максимальной
кучи в уже отсортированной до этого локальной куче. Например, как сейчас, на
последней итерации, локальная куча с индексом 2 перестала быть максимальной,
так как родительским элементом стало значение 7, при этом есть потомок со
значением 8. В таком случае мы должны рекурсивно пройти по отсортированным
ранее локальным кучам и привести их к максимальным.

           15
         /    \\
        8      11
      /   \\   /  \\
     5     7 3    8
    / \\   /
   2   4 0

Теперь дерево имеет вид максимальной кучи, а наш массив array = [15,8,11,5,7,3,8,2,4,0]
После того как мы нашли максимальный элемент, теперь он на первом месте массива,
поменяем его местами с последним элементом массива: array = [0,8,11,5,7,3,8,2,4,15].
    """)
    input('Нажмите Enter для продолжения...')
    print("""Повторим нахождение максимальной кучи, но в этот раз не будем брать последний элемент, так как
он уже в отсортированном положении на последнем месте массива: array = [0,8,11,5,7,3,8,2,4,  15]

Теперь за стартовый индекс в алгоритм передадим индекс -> ((len(list) - 1) // 2), что
соответствует 4. Дерево примет следующий вид:

           0            <- элемент и его индекс ->              1
        /     \\                                              /     \\
       8       11       <- элемент и его индекс ->          2       3
     /   \\    /  \\                                        /   \\    /  \\
    5     7  3    8     <- элемент и его индекс ->       4     5  6    7
   / \\                                                  / \\
  2   4                 <- элемент и его индекс ->     8   9
    """)
    input('Нажмите Enter для продолжения...')
    print("""Начинаем с кучи с родительским индексом
 ->        i = 4                    i = 3                   i = 2                   i = 1
     2 < 5 -> не меняем   |  3 < 11 -> не меняем  |  5 < 8 -> не меняем  |       8 > 0 -> max=8
     4 < 5 -> не меняем   |  8 < 11 -> не меняем  |  7 < 8 -> не меняем  |  11 > max -> меняем max и 0
                          |                       |                      |
               0          |            0          |            0         |           11
            /     \\       |         /     \\       |         /     \\      |         /     \\
           8       11     |        8       11     |        8       11    |        8       0
         /   \\    /  \\    |      /   \\    /  \\    |      /   \\    /  \\   |      /   \\    /  \\
        5     7  3    8   |     5     7  3    8   |     5     7  3    8  |     5     7  3    8
       / \\                |    / \\                |    / \\               |    / \\
      2   4               |   2   4               |   2   4              |   2   4

Теперь локальная куча под индексом 3 не соответствует условиям максимальной кучи.
Рекурсивно пройдем по ней:

      под индексом 3
      3 > 0 -> max=3
      8 > max -> max и 0

             11
           /     \\
          8       8
        /   \\    /  \\
       5     7  3    0
      / \\
     2   4
    """)
    input('Нажмите Enter для продолжения...')
    print("""Снова дерево имеет вид максимальной кучи, а наш массив array = [11,8,8,5,7,3,0,2,4,  15]
После того как мы нашли максимальный элемент, теперь он на первом месте массива,
поменяем его местами с последним элементом текущего массива: array = [4,8,8,5,7,3,0,2,11,  15].

Повторим нахождение максимальной кучи, но в этот раз не будем брать два последних элемента, так
как они оба уже в отсортированном положении на последних местах массива:
array = [4,8,8,5,7,3,0,2,  11,15].

И так далее до тех пор, пока массив не будет полностью отсортирован.

    """)
    input('Нажмите Enter для продолжения...')

"""
Псевдокод:

HeapSort (A as array)  <- O(nlog(n))
    BuildMaxHeap (A)
    for i = n to 1
        swap (A[1], A[i])  # перестановка первого и последнего элемента
        n = n - 1
        HeapifyMax (A, 1)

BuildMaxHeap (A as array) <- O(log(n))  # поиск крайнего родителя (индекса последней (максимальной) локальной кучи)
    n = elements_is (A)
    for i = floor (n/2) to 1
        HeapifyMax (A, i)

HeapifyMax (A as array, i as int) <- O(log(n))  # создание максимальной кучи из постоянно уменьшаемого массива
    left = 2i
    right = 2i + 1

    if (left <= n) and (A[left] > A[i])
        max = left
    else
        max = i

    if (right <= n) and (A[right] > A[max])
        max = right

    if (max != i)
        swap (A[i], A[max])
        HeapifyMax (A, max)
"""