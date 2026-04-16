class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #create variables for count, maxHeap, time, queue
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        time = 0
        q = deque()

        #while the maxheap or queue is available
        while maxHeap or q:

            #increment time
            time += 1
        
            # if maxHeap is empty then check time from queue
            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            # else take max from maxHeap, decrement it and add to queue with cooldown
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
            # return time
        return time