class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for word in strs:
            track = [0] * 26
            for char in word:
                track[ord(char) - ord('a')] += 1
            
            keys = tuple(track)
            
            if keys not in res:
                res[keys] = []
            res[keys].append(word)
        
        out = []
        for value in res.values():
            out.append(value)
        return out