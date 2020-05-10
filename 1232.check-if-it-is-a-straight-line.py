#
# @lc app=leetcode id=1232 lang=python3
#
# [1232] Check If It Is a Straight Line
#
# https://leetcode.com/problems/check-if-it-is-a-straight-line/description/
#
# algorithms
# Easy (46.59%)
# Likes:    227
# Dislikes: 32
# Total Accepted:    41.2K
# Total Submissions: 84.7K
# Testcase Example:  '[[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]'
#
# You are given an array coordinates, coordinates[i] = [x, y], where [x, y]
# represents the coordinate of a point. Check if these points make a straight
# line in the XY plane.
# 
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 2 <= coordinates.length <= 1000
# coordinates[i].length == 2
# -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
# coordinates contains no duplicate point.
# 
# 
#

# @lc code=start
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        vertical = True if coordinates[0][0] == coordinates[1][0] else False
        if vertical:
            x = coordinates[0][0]
            return all([y[0]==x for y in coordinates[1:]])
        else:
            slope = (coordinates[0][1] - coordinates[1][1])/(coordinates[0][0]-coordinates[1][0])
            intercept = coordinates[0][1] - slope * coordinates[0][0]
            return all([y[1] ==  slope * y[0]+intercept for y in coordinates[1:]])
# @lc code=end

