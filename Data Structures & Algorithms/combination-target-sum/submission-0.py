class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        total = 0
        res = []
        def backtrack(startIndex, path):
            nonlocal total
            if total == target:
                res.append(path.copy())
                return 
            if total > target:
                return
            
            for i in range(startIndex, len(nums)):
                total += nums[i]
                path.append(nums[i])
                backtrack(i, path)
                total -= nums[i]
                path.pop()
            
        backtrack(0,[])
        return res


        