from collections import deque, defaultdict

class Solution:
    def alienOrder(self, words: list[str]) -> str:
        # 1. 初始化图和入度表
        adj = defaultdict(set) # 使用 set 防止重复边
        indegree = {char: 0 for word in words for char in word}
        
        # 2. 建立偏序图
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[j := i + 1]
            min_len = min(len(w1), len(w2))
            
            # 检查前缀错误情况：如 ["abc", "ab"]
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            
            for k in range(min_len):
                if w1[k] != w2[k]:
                    if w2[k] not in adj[w1[k]]:
                        adj[w1[k]].add(w2[k])
                        indegree[w2[k]] += 1
                    break
        
        # 3. Kahn 算法进行拓扑排序
        queue = deque([u for u in indegree if indegree[u] == 0])
        ans = []
        
        while queue:
            char = queue.popleft()
            ans.append(char)
            for neighbor in adj[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # 4. 检查是否有环（排序后的字符数是否等于总字符数）
        return "".join(ans) if len(ans) == len(indegree) else ""


            
            