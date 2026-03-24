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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)  
        alse = set()
        for i in edges:
            x,y = i[0],i[1]
            dsu.union(x, y)
        for j in range(n):
            alse.add(dsu.find(j))
        return len(alse)


        
        