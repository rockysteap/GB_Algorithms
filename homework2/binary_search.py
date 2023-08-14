def binary_search(lst, value):
    res_lst = []
    left = 0
    right = len(lst) - 1
    current = (right + left) // 2
    while right >= left:
        if lst[current] == value:
            res_lst.append(current)
            first_found = current
            while current > -1:
                current -= 1
                if lst[current] == value:
                    res_lst.append(current)
                else:
                    break
            current = first_found
            while current < len(lst) - 1:
                current += 1
                if lst[current] == value:
                    res_lst.append(current)
                else:
                    break
            return res_lst
        if lst[current] < value:
            left = current + 1
        else:
            right = current - 1
        current = (right + left) // 2
    return res_lst
