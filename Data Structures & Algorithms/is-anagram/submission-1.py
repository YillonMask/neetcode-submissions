class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word = [0] * 26
        for char in s:
            word[ord(char) - ord('a')] += 1
        
        for char in t:
            word[ord(char) - ord('a')] -= 1
        
        for num in word:
            if num != 0:
                return False
        
        return True