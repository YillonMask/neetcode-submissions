class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker = {}
        for num in nums:
            if num not in tracker:
                tracker[num] = 0
            tracker[num] += 1
        
        # sort the entire value and return top k -> O(nlogn)
        sorted_tracker = dict(sorted(tracker.items(), key=lambda item:item[1], reverse=True))

        return list(sorted_tracker.keys())[:k]