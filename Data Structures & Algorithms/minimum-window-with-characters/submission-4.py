class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        have = 0
        need = len(set(t))
        count_t = Counter(t)
        res = ""
        shortest = float('inf')
        for right in range(len(s)):
            if s[right] in count_t:
                count_t[s[right]] -= 1
                if count_t[s[right]] == 0:
                    have += 1
            while left <= right and have == need:
                if right - left + 1 < shortest:
                    res = s[left:right+1]
                    shortest = right - left + 1
                if s[left] in count_t:
                    count_t[s[left]] += 1
                    if count_t[s[left]] > 0:
                        have -= 1
                left += 1
        return res

        