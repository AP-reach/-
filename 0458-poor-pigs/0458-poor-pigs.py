class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        times = minutesToTest//minutesToDie
        ans = 0
        while (times + 1)**ans < buckets:
            ans += 1
        return ans
        