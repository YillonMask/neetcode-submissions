# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # use preorder traverse the tree and store the result in a list
        res = []
        def dfs(root):
            if not root:
                res.append("N")
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        # convert the list to a str with , as delimiter
        dfs(root)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # convert the string to list using , as delemiter
        tree = data.split(",")
        idx = 0
        def dfs():
            nonlocal idx
            if tree[idx] == "N":
                idx += 1
                return None
            root = TreeNode(int(tree[idx]))
            idx += 1
            root.left = dfs()
            root.right = dfs()

            return root
        return dfs()
