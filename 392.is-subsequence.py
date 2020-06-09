#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#
# https://leetcode.com/problems/is-subsequence/description/
#
# algorithms
# Easy (47.99%)
# Likes:    1297
# Dislikes: 195
# Total Accepted:    182K
# Total Submissions: 373.5K
# Testcase Example:  '"abc"\n"ahbgdc"'
#
# Given a string s and a string t, check if s is subsequence of t.
# 
# A subsequence of a string is a new string which is formed from the original
# string by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters. (ie, "ace" is a
# subsequence of "abcde" while "aec" is not).
# 
# Follow up:
# If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you
# want to check one by one to see if T has its subsequence. In this scenario,
# how would you change your code?
# 
# Credits:
# Special thanks to @pbrother for adding this problem and creating all test
# cases.
# 
# 
# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 100
# 0 <= t.length <= 10^4
# Both strings consists only of lowercase characters.
# 
# 
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr_s, ptr_t = 0, 0
        len_s, len_t = len(s), len(t)
        while ptr_s < len_s and ptr_t < len_t:
            if s[ptr_s] == t[ptr_t]:
                ptr_s += 1
            ptr_t += 1
        return ptr_s == len_s
# @lc code=end

