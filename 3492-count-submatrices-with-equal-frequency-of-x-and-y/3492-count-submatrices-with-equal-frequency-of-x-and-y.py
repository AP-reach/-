class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        s = [[[0, 0] for _ in range(n + 1)] for _ in range(m + 1)]
        ans = 0
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                s[i + 1][j + 1][0] = s[i + 1][j][0] + s[i][j + 1][0] - s[i][j][0]
                s[i + 1][j + 1][1] = s[i + 1][j][1] + s[i][j + 1][1] - s[i][j][1]
                if c != '.':
                    s[i + 1][j + 1][ord(c) & 1] += 1
                if s[i + 1][j + 1][0] == s[i + 1][j + 1][1] > 0:
                    ans += 1
        return ans




