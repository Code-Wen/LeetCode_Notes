#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
# https://leetcode.com/problems/single-number/description/
#
# algorithms
# Easy (65.25%)
# Likes:    4552
# Dislikes: 163
# Total Accepted:    896.9K
# Total Submissions: 1.4M
# Testcase Example:  '[2,2,1]'
#
# Given a non-empty array of integers, every element appears twice except for
# one. Find that single one.
# 
# Note:
# 
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
# 
# Example 1:
# 
# 
# Input: [2,2,1]
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: [4,1,2,1,2]
# Output: 4
# 
# 
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res
# @lc code=end

