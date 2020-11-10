""" 
# MERGE INTERVALS

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

Constraints:

intervals[i][0] <= intervals[i][1] 
"""

def merge(intervals):
    if len(intervals) == 0:
        return []
    intervals.sort(key = initial)
    result = [intervals[0]]
    
    for t in intervals:
        x = result[len(result) - 1]
        if x[1] >= t[0]:
            x[1] = max(x[1], t[1])
        else:
            result.append(t)
            
    return result
    
def initial(interval):
    return interval[0]