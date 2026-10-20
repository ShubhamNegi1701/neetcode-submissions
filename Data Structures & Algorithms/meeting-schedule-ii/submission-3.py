"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda interval: interval.start)

        endTimes = []
        heapq.heapify(endTimes)

        roomsNeeded = 0

        for interval in intervals:
            start = interval.start
            end = interval.end

            while endTimes and endTimes[0] <= start:
                heapq.heappop(endTimes)
            
            heapq.heappush(endTimes, end)

            roomsNeeded = max(len(endTimes), roomsNeeded)
        return roomsNeeded

        