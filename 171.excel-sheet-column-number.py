#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#
# https://leetcode.com/problems/excel-sheet-column-number/description/
#
# algorithms
# Easy (54.21%)
# Likes:    1126
# Dislikes: 160
# Total Accepted:    309.1K
# Total Submissions: 559.1K
# Testcase Example:  '"A"'
#
# Given a column title as appear in an Excel sheet, return its corresponding
# column number.
# 
# For example:
# 
# 
# ⁠   A -> 1
# ⁠   B -> 2
# ⁠   C -> 3
# ⁠   ...
# ⁠   Z -> 26
# ⁠   AA -> 27
# ⁠   AB -> 28 
# ⁠   ...
# 
# 
# Example 1:
# 
# 
# Input: "A"
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: "AB"
# Output: 28
# 
# 
# Example 3:
# 
# 
# Input: "ZY"
# Output: 701
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 7
# s consists only of uppercase English letters.
# s is between "A" and "FXSHRXW".
# 
# 
#

# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:
        res, power = 0, 1
        for i in range(1,len(s)+1):
            res += power*(ord(s[-i])-ord('A')+1)
            power *= 26
        return res
# @lc code=end

