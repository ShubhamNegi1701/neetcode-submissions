class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max heaps dont exist in python so multiply by -1 for same effect
        stones = [-s for s in stones]
        #heapify
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
        
        stones.append(0)
        return abs(stones[0])