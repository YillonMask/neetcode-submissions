class MedianFinder:

    def __init__(self):
        # max heap for smaller half
        self.smaller = []
        # min heap for larger half
        self.larger = []
        self.size = 0

    def addNum(self, num: int) -> None:
        # if num <= greatest of smaller half
        if self.smaller and num <= -(self.smaller[0]):
            heapq.heappush(self.smaller, -num)
        # if num >= smallest of greater half
        elif self.larger and num >= self.larger[0]:
            heapq.heappush(self.larger, num)
        # other than that, does not matter which half, sent it larger
        else:
            heapq.heappush(self.larger, num)
        
        # balance heaps
        if len(self.smaller) > len(self.larger) + 1:
            val = -heapq.heappop(self.smaller)
            heapq.heappush(self.larger, val)
        elif len(self.larger) > len(self.smaller) + 1:
            val = heapq.heappop(self.larger)
            heapq.heappush(self.smaller, -val)        

    def findMedian(self) -> float:
        if len(self.larger) == len(self.smaller):
            # if two size equal, means we have even lengh
            # return the mean of root of two heap
            return (self.larger[0] - self.smaller[0]) / 2
        elif len(self.larger) > len(self.smaller):
            return self.larger[0]
        else:
            return -self.smaller[0]
        
        
        