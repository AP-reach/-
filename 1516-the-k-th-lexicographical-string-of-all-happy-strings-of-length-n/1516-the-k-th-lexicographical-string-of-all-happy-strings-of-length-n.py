class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total = 3 * (2 ** (n - 1))
        if k > total:
            return ""

        alphabet = ['a', 'b', 'c']
        block = 2 ** (n - 1)

        # 第一位
        idx = (k - 1) // block
        first = alphabet[idx]
        res = first
        k -= idx * block

        prev = first

        # 后面每一位
        for i in range(n - 1):
            block //= 2
            options = [c for c in alphabet if c != prev]

            idx = (k - 1) // block
            chosen = options[idx]

            res += chosen
            prev = chosen
            k -= idx * block

        return res


