class Solution:
    '''
    idea is to convert "lengh#str1length#str2lengthstr3...."
    "[[str1], [str2], [str3] ...]"
    '''
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        
        return "".join(res)


    def decode(self, s: str) -> List[str]:
        res = []
        if not s:
            return res
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res
