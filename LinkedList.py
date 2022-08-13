class Node():
    """Represents a node in a linked list"""
    def __init__(self,item):
        self.data = item
        self.next = None

    def __str__(self):
        return str(self.data)

class LinkedList():
    """Represents a single linked list"""
    def __init__(self):
        self.head = None

    def add(self, new_item):
        """Creates a new node with new item and add to the front"""
        node = Node(new_item)
        node.next = self.head
        self.head = node
        return self.head

    def delete(self, item):
        """Deletes the target item from the lined list, if exists"""
        # case 2: delete head
        if self.head.data == item:
            self.head = self.head.next
            return self.head
        # case 1: DELETE the middle node
        prev = None
        curr = self.head
        while curr and curr.data != item:
            prev = curr
            curr = curr.next
        if curr:
            prev.next = curr.next
        return self.head


    def __str__(self):
        """Returns all the nodes from head in a list"""
        output = []
        curr = self.head
        while curr:
            output.append(curr.data)
            curr = curr.next
        return str(output)

llist = LinkedList()
llist.add(5)
llist.add(10)
llist.add(15)
llist.add(20)
llist.delete(20)
print(llist)