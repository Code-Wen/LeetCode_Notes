#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#
# https://leetcode.com/problems/island-perimeter/description/
#
# algorithms
# Easy (63.85%)
# Likes:    1926
# Dislikes: 113
# Total Accepted:    201.4K
# Total Submissions: 311.9K
# Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
#
# You are given a map in form of a two-dimensional integer grid where 1
# represents land and 0 represents water.
# 
# Grid cells are connected horizontally/vertically (not diagonally). The grid
# is completely surrounded by water, and there is exactly one island (i.e., one
# or more connected land cells).
# 
# The island doesn't have "lakes" (water inside that isn't connected to the
# water around the island). One cell is a square with side length 1. The grid
# is rectangular, width and height don't exceed 100. Determine the perimeter of
# the island.
# 
# 
# 
# Example:
# 
# 
# Input:
# [[0,1,0,0],
# ⁠[1,1,1,0],
# ⁠[0,1,0,0],
# ⁠[1,1,0,0]]
# 
# Output: 16
# 
# Explanation: The perimeter is the 16 yellow stripes in the image below:
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def islandPerimeter_DFS(self, grid: List[List[int]]) -> int:
        """
        DFS solution. 
        """
        def dfs(i,j, grid):
            res, seen, toCheck = 0, set([(i,j)]), [(i,j)]
            while toCheck:
                x,y = toCheck.pop()
                for x1, y1 in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    if 0 <= x1 < len(grid) and 0<= y1 < len(grid[0]):
                        if grid[x1][y1] == 0:
                            res += 1
                        else:
                            if (x1,y1) not in seen:
                                toCheck.append((x1,y1))
                                seen.add((x1,y1))
                    else:
                        res += 1
            return res
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]: 
                    return dfs(i,j,grid)
                    
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res, m, n = 0, len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]: 
                    add = 4
                    for i1,j1 in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                        if 0<=i1<m and 0<=j1<n and grid[i1][j1]:
                            add -= 1
                    res += add
        return res
# @lc code=end

