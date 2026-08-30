class TreeNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            idx = ord(c) - ord("a")
            if cur.children[idx] == None:
                cur.children[idx] = TreeNode()
            cur = cur.children[idx]
        
        cur.isEnd = True


    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            idx = ord(c) - ord("a")
            if cur.children[idx] == None:
                return False
            cur = cur.children[idx]
        
        return cur.isEnd == True

        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            idx = ord(c) - ord("a")
            if cur.children[idx] == None:
                return False
            cur = cur.children[idx]
        
        return True
        
        