class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        al = 3*(2**(n-1))
        if k > al:
            return ''
        
        answer_sheet = []
        index = ['a','b','c']

        def fill_str( s ) -> None:
            if len(s) == n:
                answer_sheet.append(s)
                return
            
            for x in index:
                if not s or s[-1] != x:
                    fill_str(s+x)
                    


        fill_str('')

        return answer_sheet[k-1]


