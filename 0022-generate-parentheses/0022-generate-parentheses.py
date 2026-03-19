class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        add = '()'
        if n == 1:
            return ['()']

        allpa = self.generateParenthesis(n-1)
        count = set()
        
        for i in allpa:
            count.add(add+i)
            for j in range(1,len(i)):
                count.add(i[:j]+add+i[j:])
        ans = []

        for t in count:
            ans.append(t)   

        return ans

        