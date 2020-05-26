#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#
# https://leetcode.com/problems/contiguous-array/description/
#
# algorithms
# Medium (44.94%)
# Likes:    1346
# Dislikes: 68
# Total Accepted:    76K
# Total Submissions: 181.6K
# Testcase Example:  '[0,1]'
#
# Given a binary array, find the maximum length of a contiguous subarray with
# equal number of 0 and 1. 
# 
# 
# Example 1:
# 
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0
# and 1.
# 
# 
# 
# Example 2:
# 
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal
# number of 0 and 1.
# 
# 
# 
# Note:
# The length of the given binary array will not exceed 50,000.
# 
#

# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # diff = # of ones minus # of zeros
        d, diff, res = { 0 : -1}, 0, 0
        for i, n in enumerate(nums):
            diff += 1 if n else -1
            
            if diff in d:
                res = max(res, i-d[diff])
            else:
                d[diff] = i
        
        return res
# @lc code=end

