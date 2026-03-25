from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        graph = defaultdict(list)

        # 建图
        for a, b in prerequisites:
            graph[b].append(a)   # b -> a
            indegree[a] += 1

        # 入度为0的入队
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        visited = 0

        while q:
            node = q.popleft()
            visited += 1

            for nei in graph[node]:   # 只遍历邻居
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return visited == numCourses

        
        
