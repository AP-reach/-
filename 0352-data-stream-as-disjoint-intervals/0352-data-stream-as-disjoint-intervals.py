from typing import List

class Union:
    def __init__(self):
        self.parent = {}

        # 每个集合的区间左右端点
        self.left = {}
        self.right = {}

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        self.parent[x] = y
        self.left[y] = min(self.left[x], self.left[y])
        self.right[y] = max(self.right[x], self.right[y])

    def same(self, x, y):
        return self.find(x) == self.find(y)


class SummaryRanges:

    def __init__(self):

        self.union = Union()

    def addNum(self, value: int) -> None:

        # 已经存在，不重复添加
        if value in self.union.parent:
            return

        # 初始化并查集
        self.union.parent[value] = value
        self.union.left[value] = value
        self.union.right[value] = value

        # 尝试和左边/右边合并
        if value - 1 in self.union.parent:
            self.union.union(value, value - 1)
        if value + 1 in self.union.parent:
            self.union.union(value, value + 1)

    def getIntervals(self) -> List[List[int]]:
        """返回当前所有不相交区间"""
        reps = set(self.union.find(x) for x in self.union.parent.keys())
        intervals = [[self.union.left[r], self.union.right[r]] for r in reps]
        intervals.sort(key=lambda x: x[0])
        return intervals

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()