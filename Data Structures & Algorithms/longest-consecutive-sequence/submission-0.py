class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute force
        res = 0
        numset = set(nums)
        for i in range(len(nums)):
            cur = nums[i]
            longest = 1
            while cur + 1 in numset:
                longest += 1
                cur += 1
            res = max(res, longest)
        
        return res
