class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker = {}
        for num in nums:
            if num not in tracker:
                tracker[num] = 0
            tracker[num] += 1
        
        # sort the entire value and return top k -> O(nlogn)
        #sorted_tracker = sorted(tracker.items(), key=lambda item:item[1], reverse=True)

        #return [item[0] for item in sorted_tracker[:k]]

        # alternatively, we can use heap to store only top k
        heap = []
        for num, freq in tracker.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [item[1] for item in heap]

