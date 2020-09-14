#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#
# https://leetcode.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (56.66%)
# Likes:    1278
# Dislikes: 56
# Total Accepted:    183.4K
# Total Submissions: 317.6K
# Testcase Example:  '3\n7'
#
# 
# Find all possible combinations of k numbers that add up to a number n, given
# that only numbers from 1 to 9 can be used and each combination should be a
# unique set of numbers.
# 
# Note:
# 
# 
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# 
# 
# Example 2:
# 
# 
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]
# 
# 
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def helper(k, start, n):
            """
            Inputs:
                k: number of integers in the combination
                start: the smallest number allowed in the combination (largest is 9)
                n: goal of sum
            Returns:
                list of unique combinations
            """
            if k == 1 and start <= n <= 9:
                return [[n]]
        
            if k == 1 and (n < start or n > 9):
                return []
        
            res = []
            for i in range(start, 10):
                res += [[i] + x for x in helper(k-1, i+1, n-i)]
            
            return res
        
        return helper(k, 1, n)
# @lc code=end

