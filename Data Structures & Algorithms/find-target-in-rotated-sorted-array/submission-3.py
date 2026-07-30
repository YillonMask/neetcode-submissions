class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # first find the pivot point
        left, right = 0 , len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left
        
        # find which part does the target belongs
        right= len(nums) - 1
        if target >= nums[pivot] and target <= nums[right]:
            left, right = pivot, len(nums) - 1
        else:
            left, right = 0, pivot - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        
        return -1

            
