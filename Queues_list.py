# Queue Implementation using Lists
# Basic Operations with Queue
    # 1. enqueue(element)
    # 2. dequeue()
    # 3. is_empty()
    # 4. front()
    # 5. rear()
    # 6. size()

class Queue:
    def __init__(self) -> None:
        self.queue = []
        self.queue_size = 0
        
    def enqueue(self, data):
        self.queue.append(data)
        self.queue_size += 1
        return
    
    def dequeue(self):
        if self.is_empty():
            return None
        front = self.front()
        self.queue.remove(front)
        self.queue_size -= 1
        return front

    def is_empty(self):
        return self.queue_size == 0

    def front(self):
        if self.is_empty():
            print("Queue is empty")
            return
        else:
            return self.queue[0]

    def rear(self):
        if self.is_empty():
            print("Queue is empty")
            return
        else:
            return self.queue[-1]

    def size(self):
        return self.queue_size

