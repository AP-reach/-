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
    def solve(self, board: List[List[str]]) -> None:
        candidate = []
        m = len(board)
        n = len(board[0])

        def node(x,y):
            return x*n + y

        dsu = DSU(m*n + 1)
        boundary = m*n
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        #check through the matrix and construct the array
        #attach the boundary points to a special set

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                        dsu.union(node(i,j),boundary)
                    else:
                        for x , y in dirs:
                            ni , nj = i + x , j + y
                            if board[ni][nj] == 'O':
                                dsu.union(node(ni,nj), node(i,j))
        blank = dsu.find(boundary)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    if dsu.find(node(i,j)) != blank:
                        board[i][j] = 'X'

                        

        
        




        