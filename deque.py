class Deque:
    """ This implements a double-ended queue """

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def addFront(self, )