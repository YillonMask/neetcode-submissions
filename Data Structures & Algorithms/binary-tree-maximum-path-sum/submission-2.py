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
            # update the global maximum of path through the node
            splitSum = max(leftMax + rightMax + root.val, splitSum)
            # return the maximum of path not through the node
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return splitSum


