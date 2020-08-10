#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#
# https://leetcode.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (30.81%)
# Likes:    1260
# Dislikes: 253
# Total Accepted:    222.4K
# Total Submissions: 716.4K
# Testcase Example:  '1'
#
# Given a positive integer, return its corresponding column title as appear in
# an Excel sheet.
# 
# For example:
# 
# 
# ⁠   1 -> A
# ⁠   2 -> B
# ⁠   3 -> C
# ⁠   ...
# ⁠   26 -> Z
# ⁠   27 -> AA
# ⁠   28 -> AB 
# ⁠   ...
# 
# 
# Example 1:
# 
# 
# Input: 1
# Output: "A"
# 
# 
# Example 2:
# 
# 
# Input: 28
# Output: "AB"
# 
# 
# Example 3:
# 
# 
# Input: 701
# Output: "ZY"
# 
#

# @lc code=start
class Solution:
    def convertToTitle(self, n: int) -> str:
        lst, startORD = [], ord('A')-1
        while n:
            r, n = n%26, (n-1)//26
            if not r:
                r = 26
            lst.append(chr(r+startORD))
        return ''.join(lst[::-1])

# @lc code=end

