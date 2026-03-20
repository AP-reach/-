class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        # 1. 收集 k 个节点
        nodes = []
        cur = head
        count = 0
        while cur and count < k:
            nodes.append(cur)
            cur = cur.next
            count += 1

        # 不足 k 个，不翻转
        if count < k:
            return head

        # 2. 翻转这 k 个节点
        for i in range(k - 1, 0, -1):
            nodes[i].next = nodes[i - 1]

        # 3. 递归处理后续
        head.next = self.reverseKGroup(cur, k)

        # 新头是原第 k 个
        return nodes[-1]



        


            