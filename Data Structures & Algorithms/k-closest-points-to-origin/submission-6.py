class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for x, y in points:
            dstance = x * x + y * y 

            heapq.heappush(maxHeap, (-distance, x, y))

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        return [[x, y] for _, x, y in maxHeap]