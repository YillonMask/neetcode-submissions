class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointer
        left, right = 0, len(heights) - 1
        max_water = 0
        while left < right:
            cur_water = (right - left) * min(heights[right], heights[left])
            max_water = max(cur_water, max_water)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return max_water