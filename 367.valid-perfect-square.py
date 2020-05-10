#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#
# https://leetcode.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (41.05%)
# Likes:    733
# Dislikes: 156
# Total Accepted:    181.4K
# Total Submissions: 438.8K
# Testcase Example:  '16'
#
# Given a positive integer num, write a function which returns True if num is a
# perfect square else False.
# 
# Note: Do not use any built-in library function such as sqrt.
# 
# Example 1:
# 
# 
# 
# Input: 16
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: 14
# Output: false
# 
# 
# 
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: return True
        div = 2.0
        while abs(div*div-num) >= 1:
            div = (div+num/div)/2
        intDiv = math.floor(div)
        return any([x**2 == num for x in [intDiv-1, intDiv, intDiv+1]])
# @lc code=end

