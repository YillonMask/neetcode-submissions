class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = -1
        res = ""
        n = len(s)
        dp = [[False] * n for _ in range(len(s))]

        
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i + 1 <= 3 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if j - i + 1 > longest:
                        longest = j - i + 1
                        res = s[i : j + 1]
        return res