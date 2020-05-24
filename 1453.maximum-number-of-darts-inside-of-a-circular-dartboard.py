#
# @lc app=leetcode id=1453 lang=python3
#
# [1453] Maximum Number of Darts Inside of a Circular Dartboard
#
# https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/description/
#
# algorithms
# Hard (31.69%)
# Likes:    50
# Dislikes: 160
# Total Accepted:    2.5K
# Total Submissions: 7.8K
# Testcase Example:  '[[-2,0],[2,0],[0,2],[0,-2]]\n2'
#
# You have a very large square wall and a circular dartboard placed on the
# wall. You have been challenged to throw darts into the board blindfolded.
# Darts thrown at the wall are represented as an array of points on a 2D
# plane. 
# 
# Return the maximum number of points that are within or lie on any circular
# dartboard of radius r.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: points = [[-2,0],[2,0],[0,2],[0,-2]], r = 2
# Output: 4
# Explanation: Circle dartboard with center in (0,0) and radius = 2 contain all
# points.
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: points = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5
# Output: 5
# Explanation: Circle dartboard with center in (0,4) and radius = 5 contain all
# points except the point (7,8).
# 
# 
# Example 3:
# 
# 
# Input: points = [[-2,0],[2,0],[0,2],[0,-2]], r = 1
# Output: 1
# 
# 
# Example 4:
# 
# 
# Input: points = [[1,2],[3,5],[1,-1],[2,3],[4,1],[1,3]], r = 2
# Output: 4
# 
# 
# 
# Constraints:
# 
# 
# 1 <= points.length <= 100
# points[i].length == 2
# -10^4 <= points[i][0], points[i][1] <= 10^4
# 1 <= r <= 5000
# 
#

# @lc code=start
class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        # For two points p1, p2, if the distance <= r:
        # compute the centers C1, C2 of circles with radius r and 
        # both p1, p2 on the circle.
        # Count how many points lie in or on the circle. Update.

        # O(n^3).
        res, rSquared = 1, r*r
        for (x1, y1), (x2, y2) in itertools.combinations(points, 2):
            d = ((x1 - x2)**2 + (y1 - y2)**2) / 4.0
            if d > rSquared: continue
            x0 = (x1 + x2) / 2.0 + (y2 - y1) * (rSquared - d)**0.5 / (d * 4) ** 0.5
            y0 = (y1 + y2) / 2.0 - (x2 - x1) * (rSquared - d)**0.5 / (d * 4) ** 0.5
            res = max(res, sum((x - x0)**2 + (y - y0)**2 <= rSquared + 0.00001 for x, y in points))
        return res



# @lc code=end

