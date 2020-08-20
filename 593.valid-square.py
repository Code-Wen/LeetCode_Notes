#
# @lc app=leetcode id=593 lang=python3
#
# [593] Valid Square
#
# https://leetcode.com/problems/valid-square/description/
#
# algorithms
# Medium (43.08%)
# Likes:    257
# Dislikes: 430
# Total Accepted:    36K
# Total Submissions: 83.5K
# Testcase Example:  '[0,0]\n[1,1]\n[1,0]\n[0,1]'
#
# Given the coordinates of four points in 2D space, return whether the four
# points could construct a square.
# 
# The coordinate (x,y) of a point is represented by an integer array with two
# integers.
# 
# Example:
# 
# 
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: True
# 
# 
# 
# 
# Note:
# 
# 
# All the input integers are in the range [-10000, 10000].
# A valid square has four equal sides with positive length and four equal
# angles (90-degree angles).
# Input points have no order.
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def getVector(p1,p2):
            """
            Compute the vector from p1 to p2
            """
            return (p2[0]-p1[0], p2[1]-p1[1])
        
        def computeNorm(v):
            """
            Compute the vector norm square
            """
            return v[0]**2 + v[1]**2
        
        def dotProd(v1,v2):
            """
            Compute the dot product of two vectors
            """
            return v1[0]*v2[0]+v1[1]*v2[1]
        
        vectors = [getVector(p1, p2), getVector(p1, p3), getVector(p1,p4)]
        norms =  {}
        for v in vectors:
            norm = computeNorm(v)
            norms[norm] = norms.get(norm,[])+[v]
        if len(norms) != 2: return False
        m, M = min(norms.keys()), max(norms.keys())
        if M != 2*m or len(norms[m]) != 2: return False
        return dotProd(norms[m][0], norms[m][1]) == 0 and dotProd(norms[m][0], norms[M][0]) == dotProd(norms[m][1], norms[M][0])


# @lc code=end

