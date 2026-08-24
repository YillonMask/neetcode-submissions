# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_map = {}
        for idx, num in enumerate(inorder):
            idx_map[num] = idx
        self.pre_idx = 0
        def helper(l, r):
            if l > r:
                return None
            
            root = TreeNode(preorder[self.pre_idx])
            idx = idx_map[preorder[self.pre_idx]]
            self.pre_idx += 1

            root.left = helper(l, idx - 1)
            root.right = helper(idx + 1, r)
            return root

        return helper(0, len(inorder) - 1)
