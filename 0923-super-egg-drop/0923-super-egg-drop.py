class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp = defaultdict(int)
        for i in range(1,n+1):
            for j in range(1,k+1):
                dp[(i,j)] = (dp[(i-1,j-1)] + dp[(i-1,j)] + 1)
                if dp[(i,j)] >= n:
                    return i
    



