class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] -> maximum money from ith room
        # dp[i] = max(nums[i] + dp[i - 2], dp[i - 1] )
        
        n = len(nums)
        if n <= 1:
            return nums[0]
        dp = [-1] * (n)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        
        return dp[n - 1]