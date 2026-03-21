class Solution:
    def findDerangement(self, n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1

        l , r = 0 , 1
        for i in range(n-2):
            new = (i+2)*(l+r)
            l = r
            r = new%(10**9 + 7)
        return r