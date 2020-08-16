#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#
# https://leetcode.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (50.11%)
# Likes:    1105
# Dislikes: 86
# Total Accepted:    157.6K
# Total Submissions: 308.5K
# Testcase Example:  '"abccccdd"'
#
# Given a string which consists of lowercase or uppercase letters, find the
# length of the longest palindromes that can be built with those letters.
# 
# This is case sensitive, for example "Aa" is not considered a palindrome
# here.
# 
# Note:
# Assume the length of given string will not exceed 1,010.
# 
# 
# Example: 
# 
# Input:
# "abccccdd"
# 
# Output:
# 7
# 
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = collections.Counter(s)
        res, hasOdd = 0, 0 
        for l, count in counts.items():
            if count%2:
                res += count - 1
                hasOdd = 1
            else:
                res += count
        return res + hasOdd
# @lc code=end

