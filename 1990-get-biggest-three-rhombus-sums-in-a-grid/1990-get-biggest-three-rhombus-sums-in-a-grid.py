import heapq
from typing import List

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        
        # p1: 主对角线前缀和 (left-top to right-bottom)
        # 偏移 n 使索引不为负：(i-j) + n
        p1 = [[0] * (n + 2) for _ in range(m + 2)]
        # p2: 副对角线前缀和 (right-top to left-bottom)
        p2 = [[0] * (n + 2) for _ in range(m + 2)]
        
        for i in range(m):
            for j in range(n):
                # i+1, j+1 是为了留出边界，方便处理前缀和减法
                p1[i+1][j+1] = p1[i][j] + grid[i][j]
                p2[i+1][j+1] = p2[i][j+2] + grid[i][j]

        res = set()
        for i in range(m):
            for j in range(n):
                # 面积为 0 的菱形（单个点）
                res.add(grid[i][j])
                
                # k 为边长偏移量
                for k in range(1, m):
                    # 边界检查：确保四个顶点都在矩阵内
                    if i + 2*k >= m or j - k < 0 or j + k >= n:
                        break
                    
                    # 使用前缀和计算四条边
                    # 1. 右上边 (Top to Right)
                    s1 = p1[i+k+1][j+k+1] - p1[i][j]
                    # 2. 左上边 (Top to Left)
                    s2 = p2[i+k+1][j-k+1] - p2[i][j+2]
                    # 3. 右下边 (Right to Bottom)
                    s3 = p2[i+2*k+1][j+1] - p2[i+k][j+k+2]
                    # 4. 左下边 (Left to Bottom)
                    s4 = p1[i+2*k+1][j+1] - p1[i+k][j-k]
                    
                    # 总和 = 四边之和 - 四个顶点（因为每条边计算了两个端点，顶点被重复计算了）
                    total = s1 + s2 + s3 + s4 - grid[i][j] - grid[i+2*k][j] - grid[i+k][j-k] - grid[i+k][j+k]
                    res.add(total)
        
        # 返回前三个最大的去重结果
        return sorted(list(res), reverse=True)[:3]


        

     
            