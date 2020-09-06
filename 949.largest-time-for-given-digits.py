#
# @lc app=leetcode id=949 lang=python3
#
# [949] Largest Time for Given Digits
#
# https://leetcode.com/problems/largest-time-for-given-digits/description/
#
# algorithms
# Easy (35.58%)
# Likes:    268
# Dislikes: 543
# Total Accepted:    29.8K
# Total Submissions: 81.5K
# Testcase Example:  '[1,2,3,4]'
#
# Given an array of 4 digits, return the largest 24 hour time that can be
# made.
# 
# The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from
# 00:00, a time is larger if more time has elapsed since midnight.
# 
# Return the answer as a string of length 5.  If no valid time can be made,
# return an empty string.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,3,4]
# Output: "23:41"
# 
# 
# 
# Example 2:
# 
# 
# Input: [5,5,5,5]
# Output: ""
# 
# 
# 
# 
# Note:
# 
# 
# A.length == 4
# 0 <= A[i] <= 9
# 
# 
# 
#

# @lc code=start
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        permutations = itertools.permutations(A, 4)
        best_hour, best_minute = -1, -1
        for perm in permutations:
            hour = perm[0]*10 + perm[1]
            minute = perm[2]*10 + perm[3]
            if best_hour < hour < 24:
                if 0 <= minute < 60:
                    best_hour, best_minute = hour, minute
            elif best_hour == hour:
                if best_minute < minute < 60:
                    best_minute = minute
            else:
                continue
        if best_hour < 0:
            return ''
        hour_str = str(best_hour) if best_hour > 9 else '0'+str(best_hour)
        minute_str = str(best_minute) if best_minute > 9 else '0'+str(best_minute)
        return hour_str+':'+minute_str
# @lc code=end

