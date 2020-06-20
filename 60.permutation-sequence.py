#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#
# https://leetcode.com/problems/permutation-sequence/description/
#
# algorithms
# Medium (36.06%)
# Likes:    1503
# Dislikes: 319
# Total Accepted:    185.7K
# Total Submissions: 502.8K
# Testcase Example:  '3\n3'
#
# The set [1,2,3,...,n] contains a total of n! unique permutations.
# 
# By listing and labeling all of the permutations in order, we get the
# following sequence for n = 3:
# 
# 
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 
# 
# Given n and k, return the k^th permutation sequence.
# 
# Note:
# 
# 
# Given n will be between 1 and 9 inclusive.
# Given k will be between 1 and n! inclusive.
# 
# 
# Example 1:
# 
# 
# Input: n = 3, k = 3
# Output: "213"
# 
# 
# Example 2:
# 
# 
# Input: n = 4, k = 9
# Output: "2314"
# 
# 
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res, nums, r = '', [i for i in range(1,n+1)], k-1
        factorial = 1
        for i in range(1,n):
            factorial *= i
        
        for i in range(1,n):
            q, r = int(r//factorial), r%factorial
            res += str(nums.pop(q))
            factorial = factorial/(n-i)
            
        res += str(nums[0])
        return res
# @lc code=end

