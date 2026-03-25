from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        graph = defaultdict(list)
        ans = []

        for row in prerequisites:
            graph[row[1]].append(row[0])
            indegree[row[0]] += 1

        s = deque([u for u in range(numCourses) if indegree[u] == 0])

        while s:
            x = s.popleft()
            ans.append(x)
            for i in graph[x]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    s.append(i) 
        return ans if len(ans) == numCourses else [] 


        
        