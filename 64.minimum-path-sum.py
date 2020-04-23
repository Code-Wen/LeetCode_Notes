#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (52.45%)
# Likes:    2479
# Dislikes: 53
# Total Accepted:    361.4K
# Total Submissions: 687.8K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right which minimizes the sum of all numbers along its path.
# 
# Note: You can only move either down or right at any point in time.
# 
# Example:
# 
# 
# Input:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
# 
# 
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        for j in range(1,n):
            grid[0][j] += grid[0][j-1]
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        
        for i in range(1,m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]
# @lc code=end

