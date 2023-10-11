# Linked List Implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None

class LinkedList:
    def __init__(self):
        self.head_node = None
        self.ll_size = 0

    # Print List
    def print_list(self):
        if self.head_node is None:
            print("List is Empty")
            return
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end = "->")
            temp = temp.next_element
        print(temp.data)
        return

    # Insertion
    # Insert at head
    # O(1)
    def insert_at_head(self, data):
        if self.head_node is not None:
            temp = self.head_node
            self.head_node = Node(data)
            self.head_node.next_element = temp
        else:
            self.head_node = Node(data)
        self.ll_size += 1
        return

    # Insert at tail
    # O(n)
    def insert_at_tail(self, data):
        if self.head_node is None:
            self.head_node = Node(data)
        else:
            temp = self.head_node
            while temp.next_element is not None:
                temp = temp.next_element
            temp.next_element = Node(data)
        self.ll_size += 1
        return

    # Deletion
    # Delete at head
    # O(1)
    def delete_at_head(self):
        if self.head_node is None:
            print("List is empty!!")
        else:
            temp = self.head_node
            self.head_node = temp.next_element
            del temp
            self.ll_size -= 1
        return

    # Delete at tail
    # O(n)
    def delete_at_tail(self):
        if self.head_node is None:
            print("List is Empty")
        else:
            prev = self.head_node
            forward = self.head_node
            while forward.next_element is not None:
                prev = forward
                forward = forward.next_element
            prev.next_element = None
            del forward
            self.ll_size -= 1
        return

    # Delete by value
    def delete_by_value(self, value):
        if self.head_node is None:
            print("List is Empty")
        else:
            location = self.search(value)
            if location is False:
                return
            if location == 0:
                temp = self.head_node
                forward = temp.next_element
                self.head_node = forward
                del temp
            else:
                prev = None
                temp = self.head_node
                forward = temp.next_element
                for _ in range(1, location):
                    prev = temp
                    temp = forward
                    forward = forward.next_element
                prev.next_element = forward
                del temp
            self.ll_size -= 1
        return

    # Searching
    def search(self, value):
        count = 1
        temp = self.head_node
        while temp is not None:
            if temp.data == value:
                return count
            count += 1
            temp = temp.next_element
        print("Value not Found")
        return False

    # Updating
    def update_value(self, old, new):
        location = self.search(old)
        if location is False:
            return
        temp = self.head_node
        for _ in range(1, location):
            temp = temp.next_element
        temp.data = new
        return

    # Extract Values
    def extract_values(self):
        values = []
        temp = self.head_node
        while temp and temp.next_element is not None:
            values.append(temp.data)
            temp = temp.next_element
        values.append(temp.data)
        return values

    # Sorting
    def sort(self):
        values = self.extract_values()
        values.sort()
        temp = self.head_node
        node_no = 0
        while temp and temp.next_element is not None:
            temp.data = values[node_no]
            temp = temp.next_element
            node_no += 1
        temp.data = values[node_no]
        return  

    # Size of Linked List
    def size(self):
        return self.ll_size             


if __name__ == "__main__":
    SLL = LinkedList()
    for i in range(0, 11):
        SLL.insert_at_tail(i)
    SLL.print_list()