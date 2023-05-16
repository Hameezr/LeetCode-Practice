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