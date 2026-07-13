class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int)
        for idx, num in enumerate(nums):
            complement = target - num
            if complement not in seen:
                seen[num] = idx
            else:
                return[seen[complement], idx]
        