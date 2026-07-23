class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        left, right = 0, 0
        most_freq = 0
        freq = defaultdict(int)
        for right in range(len(s)):
            freq[s[right]] += 1
            most_freq = max(most_freq, freq[s[right]])

            while left < right and (right - left + 1 - most_freq > k):
                freq[s[left]] -= 1
                left += 1
            
            longest = max(longest, right - left + 1)
        
        return longest