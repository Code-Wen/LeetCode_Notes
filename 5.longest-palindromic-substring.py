#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (29.30%)
# Likes:    7456
# Dislikes: 558
# Total Accepted:    987.5K
# Total Submissions: 3.4M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
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

