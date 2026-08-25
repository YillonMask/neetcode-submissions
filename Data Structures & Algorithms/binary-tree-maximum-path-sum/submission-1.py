# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        splitSum = float('-inf')
        def dfs(root):
            nonlocal splitSum
            if not root:
                return 0
            
            leftMax = max(dfs(root.left), 0)
            rightMax = max(dfs(root.right), 0)

            splitSum = max(leftMax + rightMax + root.val, splitSum)
        
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return splitSum


