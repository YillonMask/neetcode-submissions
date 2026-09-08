class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def helper(house):
            n = len(house)
            if n <= 1:
                return house[0]
            rob1 = house[0]
            rob2 = max(house[0], house[1])

            for i in range(2, len(house)):
                most = max(house[i] + rob1, rob2)
                rob1 = rob2
                rob2 = most
            
            return rob2
        
        with_first = helper(nums[0: len(nums) - 1])
        with_last = helper(nums[1:])

        return max(with_first, with_last)