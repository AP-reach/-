import random

class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self):
        while True:
            # 在正方形内采样：[-R, R]
            tx = random.uniform(-self.r, self.r)
            ty = random.uniform(-self.r, self.r)
            # 拒绝采样判断：是否在圆内
            if tx**2 + ty**2 <= self.r**2:
                return [self.x + tx, self.y + ty]

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()