class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # only start building a sequence if nums[i] - 1 is not in set
        res = 0
        numset = set(nums)
        n = len(nums)
        for i in range(n):
            cur = nums[i]
            longest = 1
            if nums[i] - 1 not in numset:
                while cur + 1 in numset:
                    cur = cur + 1
                    longest = longest + 1
            res = max(longest, res)
        
        return res