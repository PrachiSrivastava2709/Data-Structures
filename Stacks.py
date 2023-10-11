# Stack Implementation
# Basic Operations on Stack
    # 1. push()
    # 2. pop()
    # 3. peek() or top()
    # 4. isEmpty()
    # 5. size()
    # 6. print_stack()

class Stack:
    def __init__(self):
        self.stack = []
        self.stack_size = 0

    def isEmpty(self):
        return self.stack_size == 0

    def push(self, data):
        self.stack.append(data)
        self.stack_size += 1
        return

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
            return None
        self.stack_size -= 1
        return self.stack.pop()

    def top(self):
        if self.isEmpty():
            return None
        return self.stack[-1]

    def size(self):
        return self.stack_size

    def print_stack(self):
        if self.isEmpty():
            print("Stack is Empty")
            print("[]")
            return
        for data in self.stack:
            print(data, end = " ")
        print()
        return

if __name__ == "__main__":
    Stk = Stack()
    print(Stk.top())
    for i in range(3,5):
        Stk.push(i)
    print(Stk.top())
    print(Stk.size())
    print(Stk.pop())
    print(Stk.size())
    Stk.print_stack()