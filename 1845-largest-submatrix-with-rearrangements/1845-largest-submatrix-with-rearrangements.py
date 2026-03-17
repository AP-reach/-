class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m  = len(matrix)
        ans = 0
        n = len(matrix[0])
        ones = defaultdict(int)
        for i in range(m):
            count = [0]*n
            for j in range(n):
                if matrix[i][j] == 1 and i == 0:
                    ones[(i,j)] += 1
                    count[j] += 1
                elif matrix[i][j] == 1:
                    ones[(i,j)] = ones[(i-1,j)] + 1
                    count[j] = ones[(i-1,j)] + 1
                else:
                    ones[j] = 0
            count.sort(reverse= True)
            first = count[0]
            for k in range(n):
                    first = min(first,count[k])
                    area = (k+1)*first
                    ans = max(ans , area)
        return ans

                




        