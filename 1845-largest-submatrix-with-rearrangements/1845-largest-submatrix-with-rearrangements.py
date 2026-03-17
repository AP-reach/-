class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n = len(matrix[0])
        heights = [0] * n
        idx = list(range(n))  # 按照高度排序后的列号
        ans = 0

        for row in matrix:
            zeros = []
            non_zeros = []
            for j in idx:
                if row[j] == 0:
                    heights[j] = 0
                    zeros.append(j)
                else:
                    heights[j] += 1
                    non_zeros.append(j)
            idx = zeros + non_zeros  # 把高度为 0 的列号排在其他高度前面

            # heights[idx[i]] 是递增的
            for i in range(len(zeros), n):  # 高度 0 无需计算
                ans = max(ans, (n - i) * heights[idx[i]])

        return ans



                




        