class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        allset = set(nums)
        ans = 0
        for i in allset:
            if not i-1 in allset:
                j = i 
                count = 1

                while j + 1 in allset:
                    j += 1
                    count += 1

                ans = max(ans,count)
        return ans

