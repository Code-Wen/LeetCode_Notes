#
# @lc app=leetcode id=436 lang=python3
#
# [436] Find Right Interval
#
# https://leetcode.com/problems/find-right-interval/description/
#
# algorithms
# Medium (45.48%)
# Likes:    561
# Dislikes: 175
# Total Accepted:    53.7K
# Total Submissions: 112.5K
# Testcase Example:  '[[1,2]]'
#
# Given a set of intervals, for each of the interval i, check if there exists
# an interval j whose start point is bigger than or equal to the end point of
# the interval i, which can be called that j is on the "right" of i.
# 
# For any interval i, you need to store the minimum interval j's index, which
# means that the interval j has the minimum start point to build the "right"
# relationship for interval i. If the interval j doesn't exist, store -1 for
# the interval i. Finally, you need output the stored value of each interval as
# an array.
# 
# Note:
# 
# 
# You may assume the interval's end point is always bigger than its start
# point.
# You may assume none of these intervals have the same start point.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [ [1,2] ]
# 
# Output: [-1]
# 
# Explanation: There is only one interval in the collection, so it outputs
# -1.
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: [ [3,4], [2,3], [1,2] ]
# 
# Output: [-1, 0, 1]
# 
# Explanation: There is no satisfied "right" interval for [3,4].
# For [2,3], the interval [3,4] has minimum-"right" start point;
# For [1,2], the interval [2,3] has minimum-"right" start point.
# 
# 
# 
# 
# Example 3:
# 
# 
# Input: [ [1,4], [2,3], [3,4] ]
# 
# Output: [-1, 2, -1]
# 
# Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
# For [2,3], the interval [3,4] has minimum-"right" start point.
# 
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#

# @lc code=start
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        if not intervals: return []
        if len(intervals) == 1: return [-1]
        
        d = {intervals[i][0]:i for i in range(len(intervals))}
        starts = sorted([x[0] for x in intervals])
        
        res = [-1]*len(intervals)
        for i in range(len(d)):
            l, r = intervals[i]
            right_start = self.binarySearch(starts, r)
            if right_start == None:
                res[i] = -1
            else:
                res[i] = d[right_start]
        return res
        
    def binarySearch(self, A, t):
        """
        In a sorted list A with distinct numbers, find the smallest number in A which is no less than the given number t. If no such number, return None.
        """
        if A[-1] < t: return None
        
        l, r = 0, len(A)-1
        while l < r:
            if A[l] >= t: return A[l]
            mid = (l+r)//2
            if A[mid] == t: return t
            elif A[mid] < t:
                l = mid + 1
            else:
                r = mid
        return A[l]
# @lc code=end

