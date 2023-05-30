# Problem 
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

from typing import List

from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = [0]*(max(nums)+1)
        for i in range(len(nums)):
            result[nums[i]]+=1
        return result.index(max(result))
    
# Solution using dictionary
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = defaultdict(int)
        for i in nums:
            dict[i]+=1
        return max(dict, key=dict.get)
