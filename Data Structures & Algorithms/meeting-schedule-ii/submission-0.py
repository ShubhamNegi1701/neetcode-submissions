"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        sorted_intervals = sorted(intervals, key=lambda x: x.start)

        min_heap = []

        maxRooms = 0
        for interval in sorted_intervals:
            start, end = interval.start, interval.end
            while min_heap and min_heap[0] <= start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, end)
            maxRooms = max(maxRooms, len(min_heap))

        return maxRooms
