class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        cache = [[0]*(n+1) for _ in range(m+1)]
        state = set()

        for i in range(1,m+1):
            for j in range(1,n+1):
                if (i-1,j) in state or (i,j-1) in state or (i-1,j-1) in state:
                    state.add((i,j))
                cache[i][j] = cache[i-1][j] + cache[i][j-1] - cache[i-1][j-1]
                if grid[i-1][j-1] == 'X':
                    cache[i][j] += 1
                    state.add((i,j))
                elif grid[i-1][j-1] == 'Y':
                    cache[i][j] -= 1

                
                
                if cache[i][j] == 0 and (i,j) in state:
                    count += 1

        return count

