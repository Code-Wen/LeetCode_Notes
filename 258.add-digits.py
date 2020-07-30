#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#
# https://leetcode.com/problems/add-digits/description/
#
# algorithms
# Easy (56.33%)
# Likes:    830
# Dislikes: 1118
# Total Accepted:    308.7K
# Total Submissions: 538.7K
# Testcase Example:  '38'
#
# Given a non-negative integer num, repeatedly add all its digits until the
# result has only one digit.
# 
# Example:
# 
# 
# Input: 38
# Output: 2 
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
# Since 2 has only one digit, return it.
# 
# 
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        # Let's call the result of a natural number n by iteratively adding the 
        # b-based digits the b-based digital root of n, denoted by dr_b(n).
        # Then dr_b(n) = (1) 0 if n==0; (2) b-1 if n%(b-1) ==0; (3) else n%(b-1).
        # The key observation to derive this formula is
        # if n = a_0 + a_1 * b^1 + a_2 * b^2 + ... + a_n * b^n
        # since b^k %(b-1) = 1 for any k >= 0, we have
        # dr_b(n)%(b-1) = dr_n(a_0+...+a_n)%(b-1).
        if num == 0: return 0
        return num%9 if num%9 else 9
# @lc code=end

