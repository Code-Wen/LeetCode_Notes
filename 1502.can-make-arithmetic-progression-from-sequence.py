#
# @lc app=leetcode id=1502 lang=python3
#
# [1502] Can Make Arithmetic Progression From Sequence
#
# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/description/
#
# algorithms
# Easy (73.07%)
# Likes:    146
# Dislikes: 7
# Total Accepted:    22.1K
# Total Submissions: 30.4K
# Testcase Example:  '[3,5,1]'
#
# Given an array of numbers arr. A sequence of numbers is called an arithmetic
# progression if the difference between any two consecutive elements is the
# same.
# 
# Return true if the array can be rearranged to form an arithmetic progression,
# otherwise, return false.
# 
# 
# Example 1:
# 
# 
# Input: arr = [3,5,1]
# Output: true
# Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with
# differences 2 and -2 respectively, between each consecutive elements.
# 
# 
# Example 2:
# 
# 
# Input: arr = [1,2,4]
# Output: false
# Explanation: There is no way to reorder the elements to obtain an arithmetic
# progression.
# 
# 
# 
# Constraints:
# 
# 
# 2 <= arr.length <= 1000
# -10^6 <= arr[i] <= 10^6
# 
# 
#

# @lc code=start
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) < 3: return True
        arr.sort()
        diff = arr[1]-arr[0]
        for i in range(1, len(arr)-1):
            if arr[i+1]-arr[i] != diff: return False
        return True
# @lc code=end

