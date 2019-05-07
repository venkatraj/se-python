class DataNode:
    def __init__(self, data=None, next_=None):
        self.data = data
        self.next_ = next_

    def get_next(self):
        return self.next_

    def set_next(self, next_):
        self.next_ = next_

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

