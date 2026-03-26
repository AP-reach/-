class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        count = 1
        n = len(nums)
        l,r = 0,1
        while l < r and r < n:
            if nums[l] == nums[r]:
                r += 1
            else:
                count += 1
                l += 1
                nums[l] = nums[r]
                r += 1

        return count
                