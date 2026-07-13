class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char = [0] * 26
        n = len(s)
        if n != len(t):
            return False
        
        for i in range(n):
            char[ord(s[i]) - ord('a')] += 1
            char[ord(t[i]) - ord('a')] -= 1
        
        for num in char:
            if num != 0:
                return False
        return True
