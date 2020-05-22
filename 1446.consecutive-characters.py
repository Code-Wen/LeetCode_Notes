#
# @lc app=leetcode id=1446 lang=python3
#
# [1446] Consecutive Characters
#
# https://leetcode.com/problems/consecutive-characters/description/
#
# algorithms
# Easy (64.09%)
# Likes:    58
# Dislikes: 3
# Total Accepted:    8.5K
# Total Submissions: 13.3K
# Testcase Example:  '"leetcode"'
#
# Given a string s, the power of the string is the maximum length of a
# non-empty substring that contains only one unique character.
# 
# Return the power of the string.
# 
# 
# Example 1:
# 
# 
# Input: s = "leetcode"
# Output: 2
# Explanation: The substring "ee" is of length 2 with the character 'e' only.
# 
# 
# Example 2:
# 
# 
# Input: s = "abbcccddddeeeeedcba"
# Output: 5
# Explanation: The substring "eeeee" is of length 5 with the character 'e'
# only.
# 
# 
# Example 3:
# 
# 
# Input: s = "triplepillooooow"
# Output: 5
# 
# 
# Example 4:
# 
# 
# Input: s = "hooraaaaaaaaaaay"
# Output: 11
# 
# 
# Example 5:
# 
# 
# Input: s = "tourist"
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 500
# s contains only lowercase English letters.
# 
#

# @lc code=start
class Solution:
    def maxPower(self, s: str) -> int:
        curCnt, res, curChar = 1, 1, s[0]
        for l in s[1:]:
            if l == curChar:
                curCnt += 1
                res = max(res, curCnt)
            else:
                curChar, curCnt = l, 1
        return res
# @lc code=end

