class Solution:
    def getSkyline(self, buildings):
        events = []
        for l, r, h in buildings:
            events.append((l, -h, r))
            events.append((r, 0, 0))
        
        events.sort()
        
        res = [[0, 0]]
        heap = [(0, float('inf'))]  # (height, end)

        for x, h, r in events:
            while heap[0][1] <= x:
                heapq.heappop(heap)
            
            if h != 0:
                heapq.heappush(heap, (h, r))
            
            curr = -heap[0][0]
            if res[-1][1] != curr:
                res.append([x, curr])
        
        return res[1:]