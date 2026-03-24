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
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        frame = DSU(n)
        for i in edges:
            x = i[0]
            y = i[1]
            if frame.find(x) == frame.find(y):
                return False
            frame.union(x, y)
        allset = set()
        for j in range(n):
            allset.add(frame.find(j))
        
        return True if len(allset) == 1 else False



        