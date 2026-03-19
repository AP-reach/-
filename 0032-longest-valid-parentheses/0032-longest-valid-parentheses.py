class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s) 
        l = 0
        ans = 0
        stack = [-1]

        if n <= 1:
            return 0
        
        while l < n:
            if s[l] == '(':
                stack.append(l)   
            if s[l] == ')':
                stack.pop()
                if stack != []:
                    ma = l - stack[-1]
                    ans = max(ans,ma)
                else:
                    stack.append(l)               
            l += 1
        return ans
                


        



                
