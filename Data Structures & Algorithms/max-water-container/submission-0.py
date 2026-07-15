class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force: calculate all the combination
        max_water = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                cur_water = min(heights[i],heights[j]) * (j - i)
                max_water = max(cur_water, max_water)
        
        return max_water