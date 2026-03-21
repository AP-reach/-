class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def stepmul(x):
            if x <= 1:
                return 1
            else:
                t = 1
                for i in range(1,x+1):
                    t *= i
            return t
        
        return stepmul(m+n-2)//(stepmul(m-1)*stepmul(n-1))