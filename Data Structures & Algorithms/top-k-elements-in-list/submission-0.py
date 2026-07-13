class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        sorted_freq = dict(sorted(freq.items(), key=lambda item:item[1], reverse=True))

        res = []
        for key in sorted_freq.keys():
            res.append(key)

        return res[:k]