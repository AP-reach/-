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
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        grid = defaultdict(int)
        ans = [0]
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        dsu = DSU(m*n + 1)


        def node(x,y):
            return n*x + y

        for row in positions:
            count = ans[-1]
            x,y = row[0],row[1]
            if grid[(x,y)] == 1:
                ans.append(count)
                continue
            local_count = set()
            for p,q in dirs:
                x1,y1 = x+p,y+q
                if grid[(x1,y1)] == 1:
                    local_count.add(dsu.find(node(x1,y1)))
            before = len(local_count)
            grid[(x,y)] = 1
            for p,q in dirs:
                x1,y1 = x+p,y+q
                if grid[(x1,y1)] == 1:
                    dsu.union(node(x,y), node(x1,y1))
            count = count - before + 1
            ans.append(count)

        finale = ans[1:]
        return finale



            

            



