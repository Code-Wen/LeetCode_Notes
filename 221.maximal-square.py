#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#
# https://leetcode.com/problems/maximal-square/description/
#
# algorithms
# Medium (36.63%)
# Likes:    2606
# Dislikes: 64
# Total Accepted:    227.6K
# Total Submissions: 620.8K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.
# 
# Example:
# 
# 
# Input: 
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# Output: 4
# 
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        
        m, n  = len(matrix), len(matrix[0])
        for i in range(m):
            matrix[i] = [int(x) for x in matrix[i]]
            
        vertical = copy.deepcopy(matrix)
        for j in range(n):
            for i in range(1, m):
                if vertical[i][j] == 1:
                    vertical[i][j] += vertical[i-1][j]
        res = max(max(matrix[0]),max([matrix[i][0] for i in range(m)]))
        for i in range(1, m):
            contiguous = matrix[i][0]
            for j in range(1, n):
                if matrix[i][j] == 0:
                    contiguous = 0
                else:
                    matrix[i][j] += min([matrix[i-1][j-1], contiguous, vertical[i-1][j]])
                    res =  max(res, matrix[i][j])
                    contiguous += 1
        return res**2
# @lc code=end

