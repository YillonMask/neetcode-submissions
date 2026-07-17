class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # brute force, keep track every substring and find valid longest substring
        res = 0
        n = len(s)
        for i in range(n):
            freq = defaultdict(int)
            maxfreq = 0
            for j in range(i, n):
                freq[s[j]] += 1
                maxfreq = max(maxfreq, freq[s[j]])
                if j - i + 1 - maxfreq <= k:
                    res = max(res, j - i + 1)
        return res