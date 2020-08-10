#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#
# https://leetcode.com/problems/rotting-oranges/description/
#
# algorithms
# Medium (47.47%)
# Likes:    2047
# Dislikes: 189
# Total Accepted:    129.2K
# Total Submissions: 266.1K
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
#
# In a given grid, each cell can have one of three values:
# 
# 
# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# 
# 
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten
# orange becomes rotten.
# 
# Return the minimum number of minutes that must elapse until no cell has a
# fresh orange.  If this is impossible, return -1 instead.
# 
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# 
# 
# 
# Example 2:
# 
# 
# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never
# rotten, because rotting only happens 4-directionally.
# 
# 
# 
# Example 3:
# 
# 
# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the
# answer is just 0.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] is only 0, 1, or 2.
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        lastRotten, fresh, m, n = set(), set(), len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: fresh.add((i,j))
                elif grid[i][j] == 2: lastRotten.add((i,j))
        res = 0
        while fresh and lastRotten:
            curRotten = set()
            res += 1
            while lastRotten:
                x, y = lastRotten.pop()
                for i,j in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                    if 0<=i<m and 0<=j<n and (i,j) in fresh:
                        curRotten.add((i,j))
                        fresh.remove((i,j))
            lastRotten = curRotten
        return res if not fresh else -1
# @lc code=end

