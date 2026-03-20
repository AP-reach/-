class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res_m, res_n = m - k + 1, n - k + 1
        ans = [[0] * res_n for _ in range(res_m)]
        
        for i in range(res_m):
            for j in range(res_n):
                # 提取子矩阵
                elements = []
                for r in range(i, i + k):
                    elements.extend(grid[r][j : j + k])
                
                # 排序
                elements.sort()
                
                # 遍历寻找
                min_diff = float('inf')
                found_diff = False
                
                for idx in range(1, len(elements)):
                    diff = elements[idx] - elements[idx - 1]
                    # 只考虑不同值之间的差
                    if diff > 0:
                        if diff < min_diff:
                            min_diff = diff
                        found_diff = True
                        # 差值不可能小于 1
                        if min_diff == 1:
                            break
                
                # 所有元素都相同才是 0
                ans[i][j] = min_diff if found_diff else 0
        
        return ans

