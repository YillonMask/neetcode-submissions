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
        # we can also count how many elements we already have and stop when we reach k
        res = -1
        cnt = k
        def traverse(root):
            nonlocal res, cnt
            if not root:
                return
            traverse(root.left)
            cnt -= 1
            if cnt == 0: 
                res = root.val
            traverse(root.right)
        
        traverse(root)
        return res