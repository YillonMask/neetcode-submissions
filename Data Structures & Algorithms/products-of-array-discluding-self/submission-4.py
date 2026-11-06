class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        prefix and suffix
                 [1,2,4,6]
        prefix = [1,1,2,8]
        suffix = [48,24,6,1]
        """

        prefix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        suffix = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]
        
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]
        return res
