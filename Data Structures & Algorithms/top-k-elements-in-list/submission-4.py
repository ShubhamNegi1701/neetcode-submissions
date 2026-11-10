class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        minHeap = []

        for key, count in count.items():
            heapq.heappush(minHeap, (count, key))
            
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        res = []

        for freq, key in minHeap:
            res.append(key)

        return res