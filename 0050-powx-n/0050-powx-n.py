class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
        if n == 1:
            return x  
        if n == -1:
            return 1/x

        ans = x
        y = x
        m = abs(n)

        while m != 0:
            mod = m%2
            m = m//2
            if mod == 1:
                ans *= y
            y = y*y

        ans /= x
        

        return ans if n > 0 else 1.0/ans

