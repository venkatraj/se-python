from data_node import DataNode


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        current = self.head
        data_node = DataNode(data)
        self.head = data_node
        data_node.set_next(current)

    def pop(self):
        if self.head is not None:
            current = self.head
            self.head = current.get_next()
            return current.data

    def peek(self):
        return self.head.data

    def top(self):
        return self.head.data

    def empty(self):
        return self.head is None

    def __str__(self):
        current = self.head
        output = ''
        while current:
            output += str(current.data) + ' | '
            current = current.get_next()
        return output.rstrip(' | ')

