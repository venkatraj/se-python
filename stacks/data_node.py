class DataNode:
    def __init__(self, data=None):
        self.data = data
        self.next_ = None

    def set_next(self, next_):
        self.next_ = next_

    def get_next(self):
        return self.next_
