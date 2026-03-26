class MRUQueue:

    def __init__(self, n: int):
        self.arr = [i for i in range(1,n+1)]

    def fetch(self, k: int) -> int:
        ans = self.arr[k-1]
        for i in range(k,len(self.arr)):
            self.arr[i-1] = self.arr[i]
        self.arr[-1] = ans
        return ans
        


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)