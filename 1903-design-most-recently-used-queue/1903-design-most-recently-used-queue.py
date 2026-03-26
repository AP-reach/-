class MRUQueue:
    def __init__(self, n: int):
        self.n = n
        self.max_q = 2000 # 根据题目最大调用次数调整
        self.size = n + self.max_q
        self.bit = [0] * (self.size + 1)
        self.values = [0] * (self.size + 1)
        
        # 初始填充
        for i in range(1, n + 1):
            self.values[i] = i
            self._update(i, 1)
        self.curr_end = n

    def _update(self, i: int, val: int):
        while i <= self.size:
            self.bit[i] += val
            i += i & (-i)

    def _query(self, i: int) -> int:
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & (-i)
        return s

    def fetch(self, k: int) -> int:
        # 1. 二分查找第 k 个元素所在的真实索引 idx
        low, high = 1, self.curr_end
        idx = high
        while low <= high:
            mid = (low + high) // 2
            if self._query(mid) >= k:
                idx = mid
                high = mid - 1
            else:
                low = mid + 1
        
        # 2. 提取值并“移动”
        res = self.values[idx]
        
        # 在原位置删除
        self._update(idx, -1)
        
        # 移动到新末尾
        self.curr_end += 1
        self.values[self.curr_end] = res
        self._update(self.curr_end, 1)
        
        return res
        


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)