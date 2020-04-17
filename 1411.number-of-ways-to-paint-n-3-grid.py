#
# @lc app=leetcode id=1411 lang=python3
#
# [1411] Number of Ways to Paint N × 3 Grid
#
# https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/description/
#
# algorithms
# Hard (60.66%)
# Likes:    129
# Dislikes: 5
# Total Accepted:    4.7K
# Total Submissions: 7.8K
# Testcase Example:  '1'
#
# You have a grid of size n x 3 and you want to paint each cell of the grid
# with exactly one of the three colours: Red, Yellow or Green while making sure
# that no two adjacent cells have the same colour (i.e no two cells that share
# vertical or horizontal sides have the same colour).
# 
# You are given n the number of rows of the grid.
# 
# Return the number of ways you can paint this grid. As the answer may grow
# large, the answer must be computed modulo 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# Input: n = 1
# Output: 12
# Explanation: There are 12 possible way to paint the grid as shown:
# 
# 
# 
# Example 2:
# 
# 
# Input: n = 2
# Output: 54
# 
# 
# Example 3:
# 
# 
# Input: n = 3
# Output: 246
# 
# 
# Example 4:
# 
# 
# Input: n = 7
# Output: 106494
# 
# 
# Example 5:
# 
# 
# Input: n = 5000
# Output: 30228214
# 
# 
# 
# Constraints:
# 
# 
# n == grid.length
# grid[i].length == 3
# 1 <= n <= 5000
# 
#

# @lc code=start
class Solution:
    def numOfWays(self, n: int) -> int:
        """
        DP solution. 
        two = # of ways where the last row has 2 colors
        three = # of ways where the last row has 3 colors

        Given the previous row using 3 colors:
        there are 2 ways to draw next row with 2 colors and 2 ways with 3 colors;

        Given the previous row using 2 colors:
        there are 3 ways to draw next row with 2 colors and 2 ways with 3 colors;
        """
        two, three = 6, 6
        for i in range(2, n+1):
            two, three = 2*three + 3*two, 2*three + 2*two
        return (two+three)%(10**9+7)
# @lc code=end

