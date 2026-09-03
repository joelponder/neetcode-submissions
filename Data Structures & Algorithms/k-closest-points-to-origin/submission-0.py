import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for x in points:
            heapq.heappush(pq, (-self.distance(x[0], x[1]), x))
            if len(pq) > k:
                heapq.heappop(pq)
        return list(map(lambda x: x[1], pq))


    def distance(self, a: int, b: int) -> float:
        return ((a ** 2) + (b ** 2)) ** 0.5 
    