# Problem 
# Contains Duplicate Given an integer array nums, 
# return true if any value appears at least twice in the array, and return false if every element is distinct.
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for i in range(0, len(nums)):
            if (nums[i] in hashmap):
                return True
            hashmap[nums[i]] = i

# Solution using set
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
    
# Solution using sorting
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(0, len(nums)-1):
            if (nums[i] == nums[i+1]):
                return True
        return False
    
# Solution using Counter
from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return any(i > 1 for i in Counter(nums).values())

