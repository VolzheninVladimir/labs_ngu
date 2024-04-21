class SingleQueue:
    head = None
    tail = None
    length = 0

    # элемент очереди
    class Node:
        element = None
        next_node = None

        def __init__(self, element, next_node = None):
            self.element = element
            self.next_node = next_node

    # добавление в конец очереди
    def append(self, element):
        if not self.head:
            self.head = self.Node(element)
            self.tail = self.Node(element)
            self.length += 1
            return element
        self.tail = self.Node(element)
        node = self.head 
        while node.next_node:
            node = node.next_node
        node.next_node = self.tail
        self.length += 1

    # удалить и вернуть последний элемент очереди
    def remove(self):
        if self.head == None:
            return 0
        
        head = self.head
        element = head.element
        self.head = head.next_node

        del head

        self.length -= 1

        return element

    # вернуть первый элемент очереди
    def get_value(self):
        if self.head == None:
            return 0
        return self.head.element
    
    # вывод хвоста очереди
    def get_tail(self):
        if self.tail == None:
            return 0
        return self.tail.element

    # вывод очереди
    # признаюсь, для проверки функции тестами ничего лучше не придумал, повторил фунцию to_list
    def out(self):
        node = self.head
        new_list = []
        while node:
            print(node.element)
            new_list.append(node.element)
            node = node.next_node
        return new_list 
    
    # вывод длины очереди
    def get_length(self):
        return self.length

    # Очистка очереди
    def clear(self):
        while self.head:
            head = self.head  
            self.head = head.next_node
            del head
        self.length = 0


    # функция для проверки тестов, преобразующая очередь в обычный массив
    def to_list(self):
        node = self.head
        queue_list = []
        while node:
            queue_list.append(node.element)
            node = node.next_node
        return queue_list
