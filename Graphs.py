# Different ways of Implementing Graphs
# 1. Using Dictionary
# 2. Adjacency List
# 3. Adjacency Matrix
# Adjacency List implementation is the best one, Thus implementing that only

#Adjacency List Implementation
import Linked_List

#Challenge 8
'''q = MyQueue()

    s = MyStack()
    inf = 9999
    distance = [inf] * g.vertices
    previous = [None] * g.vertices
    for vertex in range(g.vertices):
        if vertex == source:
            q.enqueue(vertex)
    distance[source] = 0
    s.push(source)
    
    while not s.is_empty():
        current = s.pop()
        visited[current] = True
        
    
            
    return -1'''

class Graph:

    def __init__(self, vertices = 0) -> None:
        self.vertices = vertices #Total number of vertices
        self.adjacency_list = []

        for i in range(vertices):
            self.adjacency_list.append(Linked_List())

    

    
