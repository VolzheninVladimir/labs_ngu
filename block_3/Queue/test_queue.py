from Queue import SingleQueue as Q

def test_append():
    mas = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]]
    queue = Q()
    for element in mas[0]:
        queue.append(element)
    q_list = queue.to_list()
    if not(q_list == mas[1]):
        return 0
    return 1


def test_remove():
    mas = [[1, 2, 3, 4, 5], [2, 3, 4, 5]]
    queue = Q()
    for element in mas[0]:
        queue.append(element)
    queue.remove()
    q_list = queue.to_list()
    if not(q_list == mas[1]):
        return 0
    return 1


def test_get_length():
    mas = [[1, 2, 3, 4, 5], [5]]
    queue = Q()
    for element in mas[0]:
        queue.append(element)
    length = queue.get_length()
    if not(length == mas[1][0]):
        return 0
    return 1


def test_clear():
    mas = [[1, 2, 3, 4, 5, 6, 7, 8, 9], []]
    queue = Q()
    for element in mas[0]:
        queue.append(element)
    queue.clear()
    q_list = queue.to_list()
    if not(q_list == mas[1]):
        return 0
    return 1


def test_out():
    mas = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]]
    queue = Q()
    for element in mas[0]:
        queue.append(element)
    q_list = queue.out()
    if not(q_list == mas[1]):
        return 0
    return 1


def test_get_value():
    mas = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1]]
    queue = Q()
    for element in mas[0]:
        queue.append(element)
    if not(queue.get_value() == mas[1][0]):
        return 0
    return 1


def test_get_tail():
    mas = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [9]]
    queue = Q()
    for element in mas[0]:
        queue.append(element)
    for element in mas[1]:
        if not(queue.get_tail() == mas[1][0]):
            return 0
    return 1

