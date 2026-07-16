class Solution:
    def trap(self, height: List[int]) -> int:
        # brute force
        res = 0
        for i in range(len(height)):
            leftmax, rightmax = height[i], height[i]
            for j in range(i):
                leftmax = max(leftmax, height[j])
            for j in range(i + 1, len(height)):
                rightmax = max(rightmax, height[j])
            res += min(leftmax, rightmax) - height[i]
        return res