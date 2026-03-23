from typing import List

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # dp[i][j][0] 表示从 (i,j) 到终点的最小乘积，dp[i][j][1] 表示最大乘积
        dp = [[[0, 0] for _ in range(n)] for _ in range(m)]
        
        # 终点
        dp[m-1][n-1] = [grid[m-1][n-1], grid[m-1][n-1]]
        
        # 初始化最后一行（只能向右）
        for j in range(n-2, -1, -1):
            val = grid[m-1][j] * dp[m-1][j+1][0]
            dp[m-1][j] = [val, val]
        
        # 初始化最后一列（只能向下）
        for i in range(m-2, -1, -1):
            val = grid[i][n-1] * dp[i+1][n-1][0]
            dp[i][n-1] = [val, val]
        
        # 从右下角向左上角填充
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                cur = grid[i][j]
                if cur == 0:
                    dp[i][j] = [0, 0]
                else:
                    # 从右边和下边来的最大最小值
                    right_max = dp[i][j+1][1]
                    right_min = dp[i][j+1][0]
                    down_max = dp[i+1][j][1]
                    down_min = dp[i+1][j][0]
                    
                    # 四种候选值
                    candidates = [
                        cur * right_max,
                        cur * right_min,
                        cur * down_max,
                        cur * down_min
                    ]
                    dp[i][j][0] = min(candidates)
                    dp[i][j][1] = max(candidates)
        
        max_product = dp[0][0][1]
        return max_product % MOD if max_product >= 0 else -1

                 
