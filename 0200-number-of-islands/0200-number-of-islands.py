class DSU:
    def __init__(self,n : int):
        self.pa = list(range(n))
        self.rn = [1]*n

    def find(self,x):
        if self.pa[x] != x:
            self.pa[x] = self.find(self.pa[x])
        return self.pa[x]

    def union(self,x,y):
        x,y = self.find(x),self.find(y)
        if x == y :
            return
        if self.rn[x] < self.rn[y]:
            x, y = y , x
        self.pa[y] = x
        self.rn[x] += self.rn[y]


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dsu = DSU(m*n + 1)

        def node(x,y):
            return x*n + y

        dirs = [(0,1),(1,0)]
        dirs1 = [(1,0)]
        dirs2 = [(0,1)]

        
        for i in range(m):
            for j in range(n) :
                if grid[i][j] == '1' and not (i== m-1 and j == n-1):
                    if j == n-1:
                        if grid[i+1][j] == '1':
                            dsu.union(node(i,j), node(i+1,j))
                    elif i == m-1:
                        if grid[i][j+1] == '1':
                            dsu.union(node(i,j), node(i,j+1))
                    else:
                        for p,q in dirs:
                            x1,y1 = i+p,j+q
                            if grid[x1][y1] == '1':
                                dsu.union(node(i,j), node(x1,y1))
                        
                        
        count = 0
        isles = set()

        for i in range(m):
            for j in range(n) :
                if grid[i][j] == '1':
                    sub = dsu.find(node(i,j))
                    if not sub in isles:
                        isles.add(sub)
                        count += 1
        return count


        

        
        