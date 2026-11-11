class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        res = [intervals[0]]

        if len(intervals) == 1:
            return res

        for i in range(1, len(intervals)):
            new_interval = intervals[i]
            new_start, new_end = new_interval

            old_start, old_end = res[-1]

            if old_end >= new_start:
                res[-1][1] = max(new_end, old_end)
            else:
                res.append(new_interval)

        return res



