#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#
# https://leetcode.com/problems/power-of-two/description/
#
# algorithms
# Easy (43.02%)
# Likes:    794
# Dislikes: 185
# Total Accepted:    324.6K
# Total Submissions: 745.6K
# Testcase Example:  '1'
#
# Given an integer, write a function to determine if it is a power of two.
# 
# Example 1:
# 
# 
# Input: 1
# Output: true 
# Explanation: 2^0 = 1
# 
# 
# Example 2:
# 
# 
# Input: 16
# Output: true
# Explanation: 2^4 = 16
# 
# Example 3:
# 
# 
# Input: 218
# Output: false
# 
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 1:
            if n%2 != 0: return False
            n //= 2
        return n > 0
# @lc code=end

