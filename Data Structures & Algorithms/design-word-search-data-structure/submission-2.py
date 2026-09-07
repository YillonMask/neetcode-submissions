class TreeNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TreeNode()
            cur = cur.children[c]
        
        cur.isEnd = True
        

    def search(self, word: str) -> bool:
        def dfs(i, node):
            cur = node
            for j in range(i, len(word)):
                c = word[j]
                if c != ".":
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
                else:
                    for child in cur.children.values():
                        if dfs(j + 1, child):
                            return True
                    return False
            return cur.isEnd

        return dfs(0, self.root)
            



        
