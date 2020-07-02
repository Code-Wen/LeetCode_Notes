#
# @lc app=leetcode id=1496 lang=python3
#
# [1496] Path Crossing
#
# https://leetcode.com/problems/path-crossing/description/
#
# algorithms
# Easy (55.98%)
# Likes:    80
# Dislikes: 2
# Total Accepted:    9.9K
# Total Submissions: 17.7K
# Testcase Example:  '"NES"'
#
# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing
# moving one unit north, south, east, or west, respectively. You start at the
# origin (0, 0) on a 2D plane and walk on the path specified by path.
# 
# Return True if the path crosses itself at any point, that is, if at any time
# you are on a location you've previously visited. Return False otherwise.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: path = "NES"
# Output: false 
# Explanation: Notice that the path doesn't cross any point more than once.
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: path = "NESWW"
# Output: true
# Explanation: Notice that the path visits the origin twice.
# 
# 
# Constraints:
# 
# 
# 1 <= path.length <= 10^4
# path will only consist of characters in {'N', 'S', 'E', 'W}
# 
# 
#

# @lc code=start
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0,0)}
        x, y, directions = 0, 0, {'N':(0,1),'S':(0,-1),'E':(1,0),'W':(-1,0)}
        for l in path:
            stepx, stepy = directions[l]
            x += stepx
            y += stepy
            if (x,y) in visited: return True
            visited.add((x,y))
        return False
        
# @lc code=end

