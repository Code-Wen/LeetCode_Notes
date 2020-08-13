#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (48.50%)
# Likes:    912
# Dislikes: 199
# Total Accepted:    301.1K
# Total Submissions: 606.1K
# Testcase Example:  '3'
#
# Given a non-negative index k where k ≤ 33, return the k^th index row of the
# Pascal's triangle.
# 
# Note that the row index starts from 0.
# 
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
# 
# Example:
# 
# 
# Input: 3
# Output: [1,3,3,1]
# 
# 
# Follow up:
# 
# Could you optimize your algorithm to use only O(k) extra space?
# 
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        prev, row = [1,1], 1
        while row < rowIndex:
            row += 1
            cur = [1]*(len(prev)+1)
            for i in range(1,len(prev)):
                cur[i] = prev[i]+prev[i-1]
            prev = cur
        return prev
# @lc code=end

