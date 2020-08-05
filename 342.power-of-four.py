#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#
# https://leetcode.com/problems/power-of-four/description/
#
# algorithms
# Easy (41.52%)
# Likes:    588
# Dislikes: 221
# Total Accepted:    170.6K
# Total Submissions: 410K
# Testcase Example:  '16'
#
# Given an integer (signed 32 bits), write a function to check whether it is a
# power of 4.
# 
# Example 1:
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
# Input: 5
# Output: false
# 
# 
# Follow up: Could you solve it without loops/recursion?
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        # bin(0) = '0b0'
        # num & (-num) is to get the rightmost nonzero bit 
        # power of 4 numbers has odd length for bin(n)
        return num > 0 and num == (num & (-num)) and len(bin(num))%2 == 1
# @lc code=end

