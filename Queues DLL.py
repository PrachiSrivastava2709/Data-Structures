# Queue Implementation using Doubly Linked List
class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert_at_head(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.tail = self.head
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
        return

    def insert_at_tail(self, data):
        newnode = Node(data)
        if self.tail is None:
            self.tail = newnode
            self.head = self.tail
        else:
            newnode.prev = self.tail
            self.tail.next = newnode
            self.tail = newnode
        return

class Queues:
    def __init__(self):
        self.queue = DoublyLinkedList()

    def enqueue(self, data):
        self.queue.insert_at_tail(data)
        return

    def dequeue(self):
        pass