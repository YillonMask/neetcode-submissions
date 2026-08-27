class MedianFinder:

    def __init__(self):
        # smaller half using max-heap
        self.smaller = []
        # greater half using min-heap
        self.greater = []
        

    def addNum(self, num: int) -> None:
        if self.smaller and num <= (-self.smaller[0]):
            heapq.heappush(self.smaller, -num)
        else:
            heapq.heappush(self.greater, num)
        
        # balance
        if len(self.smaller) > len(self.greater) + 1:
            val = heapq.heappop(self.smaller)
            heapq.heappush(self.greater, -val)
        elif len(self.greater) > len(self.smaller) + 1:
            val = heapq.heappop(self.greater)
            heapq.heappush(self.smaller, -val)

        

    def findMedian(self) -> float:
        if len(self.smaller) > len(self.greater):
            return -self.smaller[0]
        elif len(self.smaller) < len(self.greater):
            return self.greater[0]
        else:
            return (self.greater[0] - self.smaller[0]) / 2
        
        