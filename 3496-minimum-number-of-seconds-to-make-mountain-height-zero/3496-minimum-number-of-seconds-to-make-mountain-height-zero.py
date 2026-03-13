import heapq

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
        
        heap = []
        
        # 初始化
        for t in workerTimes:
            heapq.heappush(heap, (t, t, 1))
            # (当前完成时间, workerTime, 已完成次数)
        
        ans = 0
        
        for _ in range(mountainHeight):
            time, t, k = heapq.heappop(heap)
            ans = time
            
            k += 1
            new_time = time + t * k
            
            heapq.heappush(heap, (new_time, t, k))
        
        return ans
            


            

            

