# Problem
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if (nums[i]+nums[j]==target and i!=j):
                    return [i,j]
        

def main():
    nums = [2, 7, 11, 15]
    target = 18
    solution = Solution()
    result = solution.twoSum(nums, target)
    print("Indices of the two numbers:", result)

if __name__ == "__main__":
    main()