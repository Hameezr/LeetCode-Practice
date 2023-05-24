# Problem: Product of Array Except Self does not work for some test cases
# class Solution:
#     @staticmethod
#     def multiply_array(arr):
#         result = 1
#         for num in arr:
#             result *= num
#         return result

#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         result = []
#         for i in range(len(nums)):
#             numberToFilter = nums[i]
#             filteredList = [num for num in nums if num != numberToFilter]
#             result.append(Solution.multiply_array(filteredList))
#         return result