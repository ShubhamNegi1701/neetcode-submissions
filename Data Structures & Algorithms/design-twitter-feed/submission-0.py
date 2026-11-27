class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) #userId -> list of (count, tweetIds)
        self.followMap = defaultdict(set) #userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] #ordered from most recent
        minHeap = []

        self.followMap[userId].add(userId)

        # You insert only the latest tweet from each followee into the heap.
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index - 1])

        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            # When you pop the globally most recent tweet from the heap:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            #  You immediately check if that same `followeeId` has an older tweet:
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                # If they do, you push their next most recent tweet into the heap.
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
