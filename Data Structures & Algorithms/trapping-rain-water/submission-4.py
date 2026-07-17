class Solution:
    def trap(self, height: List[int]) -> int:
        # use two pointer
        n = len(height)
        left, right = 0, n - 1
        res = 0
        leftmax = height[left]
        rightmax = height[right]
        while left < right:
            if height[left] < height[right]:
                left += 1
                leftmax = max(leftmax, height[left])
                res += leftmax - height[left]
            else:
                right -= 1
                rightmax = max(rightmax, height[right])
                res += rightmax - height[right]

        return res 