#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#
# https://leetcode.com/problems/k-closest-points-to-origin/description/
#
# algorithms
# Medium (62.29%)
# Likes:    1577
# Dislikes: 110
# Total Accepted:    254.2K
# Total Submissions: 403.8K
# Testcase Example:  '[[1,3],[-2,2]]\n1'
#
# We have a list of points on the plane.  Find the K closest points to the
# origin (0, 0).
# 
# (Here, the distance between two points on a plane is the Euclidean
# distance.)
# 
# You may return the answer in any order.  The answer is guaranteed to be
# unique (except for the order that it is in.)
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: points = [[1,3],[-2,2]], K = 1
# Output: [[-2,2]]
# Explanation: 
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest K = 1 points from the origin, so the answer is just
# [[-2,2]].
# 
# 
# 
# Example 2:
# 
# 
# Input: points = [[3,3],[5,-1],[-2,4]], K = 2
# Output: [[3,3],[-2,4]]
# (The answer [[-2,4],[3,3]] would also be accepted.)
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= K <= points.length <= 10000
# -10000 < points[i][0] < 10000
# -10000 < points[i][1] < 10000
# 
# 
# 
#

# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        pointsWithDist = []
        heapq.heapify(pointsWithDist)
        for x,y in points:
            d = x*x + y*y
            if len(pointsWithDist) >= K:
                curMax, x1, y1 = heapq.heappop(pointsWithDist)
                if -curMax > d: 
                    heapq.heappush(pointsWithDist, (-d, x, y))
                else:
                    heapq.heappush(pointsWithDist, (curMax, x1, y1))
            else: 
                heapq.heappush(pointsWithDist, (-d, x, y))
        return [[x,y] for _,x,y in pointsWithDist]
# @lc code=end

