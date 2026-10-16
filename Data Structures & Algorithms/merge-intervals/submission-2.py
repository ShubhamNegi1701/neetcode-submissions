class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])

        currentInterval = intervals[0]
        res = []

        for i in range(1, len(intervals)):
            nextInterval = intervals[i]

            if nextInterval[0] <= currentInterval[1]:
                currentInterval[1] = max(currentInterval[1], nextInterval[1])
            else:
                res.append(currentInterval)
                currentInterval = nextInterval
        res.append(currentInterval)
        
        return res

