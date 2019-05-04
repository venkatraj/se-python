from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def size(self):
        return self.length

    def empty(self):
        return self.length == 0

    def value_at(self, index):
        if index > self.length - 1:
            raise IndexError('Given index is out of range')
        else:
            current = self.head
            for _ in range(index):
                current = current.get_next()
            return current.get_data()

    def push_front(self, value):
        node = Node(value)
        node.set_next(self.head)
        self.head = node
        self.length += 1

    def push_back(self, value):
        node = Node(value)
        current = self.head
        while current.get_next():
            current = current.get_next()
        current.set_next(node)
        self.length += 1

    def pop_front(self):
        node = self.head
        self.head = self.head.get_next()
        self.length -= 1
        return node.get_data()

    def pop_back(self):
        current = self.head
        while current.get_next().get_next():
            current = current.get_next()
        value = current.get_next().get_data()
        current.set_next(None)
        self.length -= 1
        return value

    def front(self):
        return self.head.get_data()

    def back(self):
        current = self.head
        while current.get_next():
            current = current.get_next()
        return current.get_data()

    def insert(self, index, value):
        if index > self.length - 1:
            raise IndexError
        current = self.head
        for _ in range(index-1):
            current = current.get_next()
        node = Node(value)
        node.set_next(current.get_next())
        current.set_next(node)
        self.length += 1

    def erase(self, index):
        current = self.head
        for _ in range(index-1):
            current = current.get_next()
        current.set_next(current.get_next().get_next())
        self.length -= 1

    def remove_value(self, value):
        current = self.head
        if current.get_data() == value:
            self.head = current.get_next()
            self.length -= 1
            return
        while current.get_next().get_data() != value:
            print(current.get_next().get_data())
            current = current.get_next().get_next()
        if current.get_next().get_data() == value:
            current.set_next(current.get_next().get_next())
            self.length -= 1

    # def reverse(self):
    #     new_lined_list = LinkedList()
    #     current = self.head
    #     while current:
    #         new_lined_list.push_front(current)
    #     return new_lined_list

    def __str__(self):
        current = self.head
        output = ''
        while current:
            output += str(current.data) + ' -> '
            current = current.get_next()
        return output.rstrip(' -> ')

