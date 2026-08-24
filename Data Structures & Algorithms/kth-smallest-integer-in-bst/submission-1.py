# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # recursively iterate the tree to get the result
        # which is sorted. O(n) O(n)
        res = -1
        cnt = k
        def traverse(root):
            nonlocal res, cnt
            if not root:
                return
            traverse(root.left)
            if cnt == 0:
                return
            cnt -= 1
            if cnt == 0: 
                res = root.val
            traverse(root.right)
        
        traverse(root)
        return res