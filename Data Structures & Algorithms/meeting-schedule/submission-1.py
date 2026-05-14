"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda i: i.start)
        
        curr_end = 0
        for i in intervals:
            if curr_end > i.start:
                return False

            curr_end = i.end

        
        return True
