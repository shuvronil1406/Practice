#LC 56. Merge Intervals
#CODE

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])#sort the intervals based on the starting value.
        result = []
        result.append(intervals[0])
        for i in range(1, len(intervals)): #iterate from the second interval
            if intervals[i][0] <= result[-1][1]: #if the first element of the current interval is less than the second element of the last appended interval, then the intervals have to be merged
                result[-1][1] = max(result[-1][1], intervals[i][1]) #the second element of the last appended interval is being updated with the max among itself and the second element of the current interval.
            else:
                result.append(intervals[i])
        return result
