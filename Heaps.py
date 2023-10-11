class MaxHeap:
    def __init__(self):
        self.heap = []

    def isEmpty(self):
        return len(self.heap) == 0

    def insert(self, val):
        self.heap.append(val)
        self.__percolateUp(len(self.heap) - 1)

    def getMax(self):
        if self.heap:
            return self.heap[0]
        return None

    def removeMax(self):
        if len(self.heap) > 1:
            maxEle = self.heap[0]
            self.swap(0, -1)
            self.heap.pop()
            self.__maxHeapify(0)
            return maxEle
        elif len(self.heap) == 1:
            maxEle = self.heap[0]
            self.heap.pop()
            return maxEle
        else:
            return None

    def __percolateUp(self, index):
        parent = (index - 1) // 2
        if index <= 0:
            return
        elif self.heap[parent] < self.heap[index]:
            self.__swap(parent, index)
            self.__percolateUp(parent)

    def __swap(self, parent, index):
        self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
        return

    def __maxHeapify(self, index):
        largest = self.__getLargest(index, index * 2 + 1, index * 2 + 2)
        if largest != index:
            self.__swap(largest, index)
            self.__maxHeapify(largest)

    def __getLargest(self, index, left, right):
        #cant do this
        # value =  max(self.heap[index], self.heap[left], self.heap[right])
        # return self.heap.index(value)
        answer = index
        if left < len(self.heap) and self.heap[answer] < self.heap[answer]:
            pass

def getSmallest(maxHeap, index, left, right):
    answer = index
    if left < len(maxHeap) and maxHeap[index] > maxHeap[left]:
        answer = left
    if right < len(maxHeap) and maxHeap[answer] > maxHeap[right]:
        answer = right
    return answer

def minHeapify(maxHeap, index):
    smallest = getSmallest(maxHeap, index, index * 2 +1, index * 2 +2)
    if smallest != index:
        maxHeap[index], maxHeap[smallest] = maxHeap[smallest], maxHeap[index]
        minHeapify(maxHeap, smallest)
    return maxHeap

def convertMax(maxHeap):
    for i in range(len(maxHeap) -1, -1, -1):
        maxHeap = minHeapify(maxHeap, i)
    return maxHeap


heap = MaxHeap()
heap.insert(9)
heap.insert(8)
heap.insert(7)
heap.insert(10)
print(heap.heap)

maxHeap = [10,9,8,7,5,3,2]

#ksmallest/ klargest: typical use case of a Heap
def findKSmallest(lst, k):
    heap = MaxHeap()
    for element in lst:
        if heap.isEmpty() or heap.getMax() > element:
            heap.insert(element) #O(log k) for 1 element
        if heap.size() > k:
            heap.removeMax() #O(log(k))
    return heap.heap
 
lst = [10, 9, 8, 12, 15, 8, 19, 21, 23]
k = 3

print("The top K elemenst of ", lst, "are", findKSmallest)

