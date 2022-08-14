class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[-1]

    def pop(self):
        self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self):
        return f"Stack = {[i for i in self.items]}"

new_stack = Stack()
print(new_stack.isEmpty())
new_stack.push(5)
new_stack.push(15)
new_stack.push(25)
print(new_stack.peek())
new_stack.pop()
print(new_stack.peek())
print(new_stack.size())
print(new_stack)