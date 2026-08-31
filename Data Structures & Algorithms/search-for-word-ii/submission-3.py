class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # use words to create trie nodes
        root = TrieNode()
        for word in words:
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.isEnd = word
        
        row, col = len(board), len(board[0])
        seen = set()
        res = []
        def dfs(i, j, node):
            if i < 0 or i >= row or j < 0 or j >= col:
                return 
            if (i, j) in seen or board[i][j] not in node.children:
                return
            
            node = node.children[board[i][j]]
            if node.isEnd:
                res.append(node.isEnd)
                node.isEnd = None
            
            seen.add((i, j))
            dfs(i + 1, j, node)
            dfs(i - 1, j, node)
            dfs(i, j + 1, node)
            dfs(i, j - 1, node)

            seen.remove((i, j))
        
        for i in range(row):
            for j in range(col):
                dfs(i,j, root)
        
        return res


        