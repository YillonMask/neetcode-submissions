# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if both p, q are None, means we reach the end and it is ok
        if not p and not q:
            return True
        # if both p,q are not None, their value needs to be same
        if p and q and p.val == q.val:
            # then we compare their left and right
            left = self.isSameTree(p.left, q.left)
            right = self.isSameTree(p.right, q.right)

            return left and right
        # other than this, it is not ok
        else:
            return False