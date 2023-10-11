class Node:
    def __init__(self, data):
        self.prev_element = None
        self.data = data
        self.next_element = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head_node = None
        self.size = 0

    # O(1)
    # Insert Node at Head
    def  insert_at_head(self, data):
        new_node = Node(data)
        if self.head_node is None:
            self.head_node = new_node
        else:
            first_node = self.head_node
            self.head_node = new_node
            new_node.next_element = first_node
            first_node.prev_element = new_node
        return

    # O(n)
    # Insert at Tail
    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head_node is None:
            self.head_node = new_node
        else:
            temp = self.head_node
            while temp.next_element is not None:
                temp = temp.next_element
            temp.next_element = new_node
            new_node.prev_element = temp
        return 
    
    # O(1)
    # Delete at Head
    def delete_at_head(self):
        if self.head_node is None:
            print("List is Empty")
            return False
        else:
            temp = self.head_node
            self.head_node = temp.next_element
            temp.prev_element = None
            del temp
        return

    # O(n)
    # Delete at Tail
    def delete_at_tail(self):
        if self.head_node is None:
            print("List is Empty")
            return False
        else:
            temp = self.head_node
            while temp.next_element is not None:
                temp = temp.next_element
            temp.prev_element.next_element = None
            del temp
            return


    def print_list(self):
        if self.head_node is None:
            print("List is Empty")
            return
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end = " <-> ")
            temp = temp.next_element
        print(temp.data, "<->", None)
        return


if __name__ == "__main__":
    DLL = DoublyLinkedList()
    for i in range(10):
        DLL.insert_at_head(i)
    DLL.print_list()
    DLL.delete_at_tail()
    DLL.delete_at_tail()
    DLL.print_list()
