# Queue Implementation using Lists
# Basic Operations with Queue
    # 1. enqueue(element)
    # 2. dequeue()
    # 3. is_empty()
    # 4. front()
    # 5. rear()
    # 6. peek() :to get the element at the front of
    # the queue without removing it

class Queue:
    def __init__(self) -> None:
        self.queue = []

