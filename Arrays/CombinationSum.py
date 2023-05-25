# Problem
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
# frequency
#  of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()  # Sort the candidates in ascending order
        self.backtrack(candidates, target, [], result, 0)
        return result

    def backtrack(self, candidates, target, combination, result, start):
        if target < 0:
            return
        if target == 0:
            result.append(combination)
            return
        for i in range(start, len(candidates)):
            # Exclude candidates that are larger than the remaining target
            if candidates[i] > target:
                break
            # Recursively generate combinations
            self.backtrack(candidates, target - candidates[i], combination + [candidates[i]], result, i)

# Explanation

# We define a function combinationSum that takes the candidates array and the target integer as input and returns a list of all unique combinations that sum up to the target.
# We start by sorting the candidates array in ascending order using the sort method. This is done to handle duplicate combinations later in the backtracking process.
# We define a helper function backtrack that performs the actual backtracking process. It takes the candidates array, the target integer, the current combination of numbers, the result list to store the valid combinations, and the start index to keep track of the candidates that have been considered.
# In the backtrack function, we check if the current target is less than 0. If so, it means we have exceeded the target and we return from the current recursion.
# If the target is 0, it means we have found a valid combination that sums up to the target. We append this combination to the result list.
# We iterate over the candidates array starting from the start index. For each candidate, we check if it is larger than the remaining target. If so, we break the loop because the remaining candidates will also be larger.
# If the candidate is valid, we recursively call the backtrack function with the updated target (subtracting the candidate), the updated combination (adding the candidate), the result list, and the current index i. This allows us to include the same candidate multiple times in the combination.
# Finally, we define an example usage by initializing the candidates array and the target, and call the combinationSum function. The result is printed to the console.