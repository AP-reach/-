from collections import defaultdict

class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        ans = ['?'] * (n + m - 1)

        # Step 1: 强制 T
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    if ans[i + j] == '?' or ans[i + j] == str2[j]:
                        ans[i + j] = str2[j]
                    else:
                        return ''

        # Step 2: 标记 fixed（被 T 覆盖的位置）
        fixed = [False] * len(ans)
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    fixed[i + j] = True

        # Step 3: 填充默认字符
        for i in range(len(ans)):
            if ans[i] == '?':
                ans[i] = 'a'

        # Step 4: 处理 F
        for i in range(n):
            if str1[i] == 'F':
                match = True
                for j in range(m):
                    if ans[i + j] != str2[j]:
                        match = False
                        break
                
                if match:
                    for j in range(m - 1, -1, -1):
                        pos = i + j
                        if not fixed[pos]:
                            ans[pos] = 'b' if str2[j] == 'a' else 'a'
                            break
                    else:
                        return ''

        return ''.join(ans)