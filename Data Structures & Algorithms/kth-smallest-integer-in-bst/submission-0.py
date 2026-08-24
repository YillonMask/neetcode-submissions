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
        def traverse(root, res):
            if not root:
                return
            traverse(root.left, res)
            res.append(root.val)
            traverse(root.right, res)
        res = []
        traverse(root, res)
        return res[k - 1]