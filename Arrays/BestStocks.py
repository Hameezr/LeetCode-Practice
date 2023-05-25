# Problem
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

from typing import List

# Solution using two for loops (brute force) - O(n^2)
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         diff = -100
#         for i in range(len(prices)):
#             for j in range(i+1,len(prices)):
#                 if(prices[j]-prices[i]>diff):
#                     diff=prices[j]-prices[i]
#         if(diff<0):
#             return 0
#         else:
#             return diff
        
# Solution using single loop (optimized) - O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        profit = 0
        for i in range(len(prices)):
            if(prices[i]<minBuy):
                minBuy = prices[i]
            elif(prices[i]-minBuy>profit):
                profit = prices[i]-minBuy
        return profit

def main():
    prices = [7,1,20,3,30,4]
    solution = Solution()
    result = solution.maxProfit(prices)
    print("Max profit is", result)

if __name__ == "__main__":
    main()