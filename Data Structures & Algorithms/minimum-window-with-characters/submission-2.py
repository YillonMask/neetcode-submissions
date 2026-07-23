class Solution:
    def minWindow(self, s: str, t: str) -> str:
       # sliding window. find a valid window and then slide the left pointer
       # to find the smallest window possible
        freq_t = Counter(t)
        shortest = len(s) + 1
        res = ""
        left = 0
        have = 0
        need = len(set(t))
        for right in range(len(s)):
            if s[right] in freq_t:
                freq_t[s[right]] -= 1
                if freq_t[s[right]] == 0:
                    have += 1
            while left <= right and have == need:
                if right - left + 1 < shortest:
                    shortest = right - left + 1
                    res = s[left:right+1]
                if s[left] in freq_t:
                    freq_t[s[left]] += 1
                    if freq_t[s[left]] > 0:
                        have -= 1
                left += 1
        return res




