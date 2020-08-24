#
# @lc app=leetcode id=497 lang=python3
#
# [497] Random Point in Non-overlapping Rectangles
#
# https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/description/
#
# algorithms
# Medium (37.80%)
# Likes:    254
# Dislikes: 421
# Total Accepted:    22.5K
# Total Submissions: 58.5K
# Testcase Example:  '["Solution", "pick", "pick", "pick"]\n[[[[1, 1, 5, 5]]], [], [], []]'
#
# Given a list of non-overlapping axis-aligned rectangles rects, write a
# function pick which randomly and uniformily picks an integer point in the
# space covered by the rectangles.
# 
# Note:
# 
# 
# An integer point is a point that has integer coordinates. 
# A point on the perimeter of a rectangle is included in the space covered by
# the rectangles. 
# ith rectangle = rects[i] = [x1,y1,x2,y2], where [x1, y1] are the integer
# coordinates of the bottom-left corner, and [x2, y2] are the integer
# coordinates of the top-right corner.
# length and width of each rectangle does not exceed 2000.
# 1 <= rects.length <= 100
# pick return a point as an array of integer coordinates [p_x, p_y]
# pick is called at most 10000 times.
# 
# 
# 
# Example 1:
# 
# 
# Input: 
# ["Solution","pick","pick","pick"]
# [[[[1,1,5,5]]],[],[],[]]
# Output: 
# [null,[4,1],[4,1],[3,3]]
# 
# 
# 
# Example 2:
# 
# 
# Input: 
# ["Solution","pick","pick","pick","pick","pick"]
# [[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
# Output: 
# [null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]
# 
# 
# 
# Explanation of Input Syntax:
# 
# The input is two lists: the subroutines called and their arguments.
# Solution's constructor has one argument, the array of rectangles rects. pick
# has no arguments. Arguments are always wrapped with a list, even if there
# aren't any.
# 
# 
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.intervals = [0]*len(rects)
        runningSum = 0
        for i in range(len(rects)):
            x1,y1,x2,y2 = rects[i]
            runningSum += (x2-x1+1)*(y2-y1+1)
            self.intervals[i] = runningSum
        self.total = self.intervals[-1]
    
            
    def pick(self) -> List[int]:
        n = random.randint(1, self.total)
        idx = self.binarySearch(n)
        x1,y1,x2,y2 = self.rects[idx]
        return [random.randint(x1,x2), random.randint(y1,y2)]
    

    def binarySearch(self, n):
        l,r = 0, len(self.intervals)-1
        while l < r:
            mid = (l+r)//2
            if self.intervals[mid] < n:
                l = mid + 1
            else:
                r = mid
        return r



        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
# @lc code=end

