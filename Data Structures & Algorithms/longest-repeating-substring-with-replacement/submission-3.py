class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window, check every char in the s, if s can have valid substring
        charset = set(s)
        res = 0
        for char in charset:
            l = 0
            count = 0
            for r in range(len(s)):
                if s[r] == char:
                    count += 1
                while r - l + 1 - count > k:
                    if s[l] == char:
                        count -= 1
                    l += 1
                res = max(res, r - l + 1)
        return res