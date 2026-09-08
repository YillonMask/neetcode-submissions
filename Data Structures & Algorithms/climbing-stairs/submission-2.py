class Solution:
    def climbStairs(self, n: int) -> int:
        # f(n) = f(n - 1) + f(n - 2)
        if n <= 2:
            return n
        pre = 2
        prePre = 1
        
        for i in range(3, n + 1):
            one = pre + prePre
            prePre = pre
            pre = one
        return one