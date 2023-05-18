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
    