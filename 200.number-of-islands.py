#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (45.26%)
# Likes:    4697
# Dislikes: 178
# Total Accepted:    623.9K
# Total Submissions: 1.4M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
# 
# Example 1:
# 
# 
# Input:
# 11110
# 11010
# 11000
# 00000
# 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input:
# 11000
# 11000
# 00100
# 00011
# 
# Output: 3
# 
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        
        m, n = len(grid), len(grid[0])
        seen = set()
        def bfs(x0,y0):
            seen.add((x0,y0))
            q = collections.deque([(x0,y0)])
            while q:
                x,y = q.popleft()
                for x1, y1 in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    if 0<=x1<m and 0<=y1<n and grid[x1][y1]=='1' and (x1,y1) not in seen:
                        seen.add((x1,y1))
                        q.append((x1,y1))
        res = 0              
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i,j) not in seen:
                    res += 1
                    bfs(i,j)
        return res
# @lc code=end

