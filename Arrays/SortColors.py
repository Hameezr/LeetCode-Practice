# Problem: Sort Colors
# Given an array nums with n objects colored red, white, or blue, sort 
# them in-place so that objects of the same color are adjacent

from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:  # Red
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            elif nums[mid] == 1:  # White
                mid += 1
            else:  # Blue
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1