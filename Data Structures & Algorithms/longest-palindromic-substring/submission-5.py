class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = -1
        res = []
        def helper(start, end):
            nonlocal longest, res
            while start >= 0 and end < len(s) and s[start] == s[end]:
                if end - start + 1 > longest:
                    longest = end - start + 1
                    res = s[start: end + 1]
                start -= 1
                end += 1
        for i in range(len(s)):
            
            l, r = i, i
            helper(l, r)

            l, r = i, i + 1
            helper(l, r)
            
        return str(res)