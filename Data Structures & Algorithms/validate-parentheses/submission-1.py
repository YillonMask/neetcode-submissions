class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {')':'(', '}':'{', ']':'['}
        stack = []
        for c in s:
            if c in bracket_dict:
                if not stack or stack[-1] != bracket_dict[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0