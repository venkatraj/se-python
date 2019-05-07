from data_node import DataNode


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, value):
        if self.size == 0:
            self.head = DataNode(value)
            self.tail = self.head
        else:
            newNode = DataNode(value)
            self.tail.set_next(newNode)
            self.tail = newNode
        self.size += 1

    def dequeue(self):
        if self.empty():
            return
        removed = self.head
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.get_next()
        self.size -= 1
        return removed.get_data()

    def empty(self):
        return self.size == 0

    def __str__(self):
        current = self.head
        output = ''
        while current:
            output += str(current.get_data()) + ' -> '
            current = current.get_next()

        return output.rstrip(' -> ')