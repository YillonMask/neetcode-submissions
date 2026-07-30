class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
    
        while left < right:
            mid = (left + right) // 2
            
            # 如果中间值大于最右侧值，说明断层在右半部分
            if nums[mid] > nums[right]:
                left = mid + 1
            # 否则，断层在左半部分或就是mid
            else:
                right = mid
                
        # 当 left == right 时，即为最小值所在索引
        return nums[left]