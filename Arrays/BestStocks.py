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