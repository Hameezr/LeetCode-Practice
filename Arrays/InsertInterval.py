# Problem
# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

from typing import List

# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         keyValue = {key_list[0]: key_list[1] for key_list in intervals}
#         newKey = 0
#         newVal = 0
#         if len(intervals) == 0:
#             intervals.append(newInterval)
#             return intervals
#         for key, value in keyValue.items():
#             if(newInterval[0]<value):
#                 if(newInterval[1] in keyValue.keys()):
#                     keyValue[key] = keyValue[newInterval[1]]
#                     newVal = keyValue[newInterval[1]]
#                     newKey = key
#                 else:
#                     keyValue[key] = newInterval[1]
#                 break
#         keyValue_copy = keyValue.copy()
#         for key, value in keyValue_copy.items():
#             if(value <= newVal and key>newKey):
#                 del keyValue[key]
#         intervals = list(keyValue.items())
#         return intervals

class Solution:
    def insert(self, intervals, newInterval):
        res = []
        i = 0

        # Add intervals that end before the new interval starts
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # Merge intervals that overlap with the new interval
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        # Add the merged interval to the result
        res.append(newInterval)

        # Add remaining intervals
        res += intervals[i:]

        return res
                

def main():
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    solution = Solution()
    result = solution.insert(intervals, newInterval)
    print("Result:", result)

if __name__ == "__main__":
    main()
