class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        s = 0
        ans = float('inf')

        for right in range(n):
            s += nums[right]

            while s >= target:
                ans = min(ans, right - left + 1)
                s -= nums[left]
                left += 1

        return 0 if ans == float('inf') else ans


            
            
