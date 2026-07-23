class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # brute force: find all possible combination of substring
        # check if there is valid one and keep track of the length
        shortest = len(s) + 1
        res = ""
        
        for i in range(len(s)):
            t_dic = Counter(t)
            for j in range(i, len(s)):
                cur_char = s[j]
                if cur_char in t_dic:
                    t_dic[cur_char] -= 1
                    if t_dic[cur_char] == 0:
                        del t_dic[cur_char]
                if not t_dic:
                    if j - i + 1 < shortest:
                        shortest = j - i + 1
                        res = s[i: j+1]
        return res