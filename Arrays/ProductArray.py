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

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_products = [1] * n
        right_products = [1] * n
        result = [1] * n
        
        # Calculate the product of all elements to the left of each element
        for i in range(1, n):
            left_products[i] = left_products[i-1] * nums[i-1]
        
        # Calculate the product of all elements to the right of each element
        for i in range(n-2, -1, -1):
            right_products[i] = right_products[i+1] * nums[i+1]
            # print (right_products)
        
        # Multiply the corresponding left and right products to get the answer
        for i in range(n):
            result[i] = left_products[i] * right_products[i]
        
        return result