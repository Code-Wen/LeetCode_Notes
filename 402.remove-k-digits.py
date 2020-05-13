#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#
# https://leetcode.com/problems/remove-k-digits/description/
#
# algorithms
# Medium (27.66%)
# Likes:    1723
# Dislikes: 88
# Total Accepted:    103.9K
# Total Submissions: 374.6K
# Testcase Example:  '"1432219"\n3'
#
# Given a non-negative integer num represented as a string, remove k digits
# from the number so that the new number is the smallest possible.
# 
# 
# Note:
# 
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.
# 
# 
# 
# 
# Example 1:
# 
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219
# which is the smallest.
# 
# 
# 
# Example 2:
# 
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output
# must not contain leading zeroes.
# 
# 
# 
# Example 3:
# 
# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with
# nothing which is 0.
# 
# 
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k or len(num) == 0: return '0'
        if k == 0: return num
        else:
            if num[1] == '0':
                i = 1
                while i < len(num) and num[i] == '0': i += 1
                return self.removeKdigits(num[i:], k-1)
            elif num[1] < num[0]:
                return self.removeKdigits(num[1:], k-1)
            else:
                i = 0
                while i+1 < len(num) and num[i+1] >= num[i]:
                    i += 1
                return self.removeKdigits(num[:i]+num[i+1:], k-1)
        

            
# @lc code=end

