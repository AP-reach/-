class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [1] * n
        
        # Step 1: Calculate Prefix products
        # ans[i] will store the product of all elements to the left of i
        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]
            
        # Step 2: Calculate Suffix products on the fly
        # Multiply current prefix (stored in ans) by the running suffix
        suffix = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]
            
        return ans

        
