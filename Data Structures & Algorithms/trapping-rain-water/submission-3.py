class Solution:
    def trap(self, height: List[int]) -> int:
        # use prefix and suffix array to keep track leftmax and rightmax
        n = len(height)
        prefix = [height[0]] * n
        suffix = [height[n - 1]] * n

        for i in range(1, n):
            prefix[i] = max(prefix[i - 1], height[i])
        
        for i in range(n - 2, -1, -1):
            suffix[i] = max(suffix[i + 1], height[i])
        

        res = 0

        for i in range(n):
            res += min(prefix[i], suffix[i]) - height[i]
        
        return res