""" for example in bank, if anyone come to withdraw money he/she needs to stay at the last of the line. The line
 will follow first in first out method. In this type of case,we will use queue"""

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def PillowPassingGame(players, passing_num):
    """Implementing quene on pillow passing game"""
    new_queue = Queue()
    for player in players:
        new_queue.enqueue(player)

    while new_queue.size() > 1:
        for i in range(passing_num):
            new_queue.enqueue(new_queue.dequeue())

        new_queue.dequeue()

    return new_queue.dequeue()

print(PillowPassingGame(['nayem', 'sourab', 'maruf', 'parvez', 'shahadat', 'pranto', 'manindra'], 26))