#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position/description/
#
# algorithms
# Easy (41.70%)
# Likes:    2244
# Dislikes: 245
# Total Accepted:    600.1K
# Total Submissions: 1.4M
# Testcase Example:  '[1,3,5,6]\n5'
#
# Given a sorted array and a target value, return the index if the target is
# found. If not, return the index where it would be if it were inserted in
# order.
# 
# You may assume no duplicates in the array.
# 
# Example 1:
# 
# 
# Input: [1,3,5,6], 5
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [1,3,5,6], 2
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: [1,3,5,6], 7
# Output: 4
# 
# 
# Example 4:
# 
# 
# Input: [1,3,5,6], 0
# Output: 0
# 
# 
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        if nums[0] >= target: return 0
        if nums[-1] == target: return r
        if nums[-1] < target: return r+1
        
        while l+1 < r:
            mid = (l+r)//2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid
        return l+1 if nums[l]<target else l
# @lc code=end

