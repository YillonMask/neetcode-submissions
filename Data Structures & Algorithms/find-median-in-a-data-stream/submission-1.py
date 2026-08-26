class MedianFinder:

    def __init__(self):
        self.heap = []
        self.size = 0

    def addNum(self, num: int) -> None:
        # O(logn)
        self.heap.append(num)
        self.heap.sort()
        self.size += 1
        

    def findMedian(self) -> float:
        # O(1)
        if self.size % 2 == 0:
            # return mean of two middle values
            return (self.heap[self.size // 2] + self.heap[self.size // 2 - 1]) / 2
        else:
            return self.heap[self.size // 2]
        
        