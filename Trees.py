class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self, data):
        self.root = Node(data)

    def insertLeft(self, value):
        if self.root.left is None:
            self.root.left = Node(value)
        else:
            new_node = Node(value)
            new_node.left = self.root.left
            self.root.left = new_node

    def insertRight(self, value):
        if self.root.right is None:
            self.root.right = Node(value)
        else:
            new_node = Node(value)
            new_node.right = self.root.right
            self.root.right = new_node























































'''# Implementation of Binary Search Tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class Tree:
    def __init__(self, data):
        self.root = Node(data)

    def print_tree(self):
        pass

    def insert_helper(self, current, data):
        current = self.root
        if current == None:
            return Node(data)
        elif data < current.data:
            current.left = self.insert_helper(self, current.left, data)
        else:
            current.right = self.insert_helper(self, current.right, data)
        return

    def insert(self, data):
        current = self.root
        parent = None

        while current is not None:
            parent = current
            if data < current.data:
                current = current.left
            else:
                current = current.right
        #parent == leaf node(while loop breaks)
        
        if data < parent.data:
            parent.left = Node(data)
        else:
            parent.right = Node(data)
        return
        node = self.insert_helper(self, self.root, data)
        return'''





        


