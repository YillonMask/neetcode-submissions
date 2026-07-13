class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        seen = set()
        longest = 0
        while right < len(s):
            while s[right] in seen and left < right:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            cur_len = right - left + 1
            if cur_len > longest:
                longest = cur_len
            right += 1
        return longest