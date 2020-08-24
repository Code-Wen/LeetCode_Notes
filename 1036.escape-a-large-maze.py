#
# @lc app=leetcode id=1036 lang=python3
#
# [1036] Escape a Large Maze
#
# https://leetcode.com/problems/escape-a-large-maze/description/
#
# algorithms
# Hard (35.40%)
# Likes:    225
# Dislikes: 99
# Total Accepted:    9.9K
# Total Submissions: 28.1K
# Testcase Example:  '[[0,1],[1,0]]\n[0,0]\n[0,2]'
#
# In a 1 million by 1 million grid, the coordinates of each grid square are (x,
# y) with 0 <= x, y < 10^6.
# 
# We start at the source square and want to reach the target square.  Each
# move, we can walk to a 4-directionally adjacent square in the grid that isn't
# in the given list of blocked squares.
# 
# Return true if and only if it is possible to reach the target square through
# a sequence of moves.
# 
# 
# 
# Example 1:
# 
# 
# Input: blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
# Output: false
# Explanation: 
# The target square is inaccessible starting from the source square, because we
# can't walk outside the grid.
# 
# 
# Example 2:
# 
# 
# Input: blocked = [], source = [0,0], target = [999999,999999]
# Output: true
# Explanation: 
# Because there are no blocked cells, it's possible to reach the target
# square.
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= blocked.length <= 200
# blocked[i].length == 2
# 0 <= blocked[i][j] < 10^6
# source.length == target.length == 2
# 0 <= source[i][j], target[i][j] < 10^6
# source != target
# 
# 
#

# @lc code=start
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        
# @lc code=end

