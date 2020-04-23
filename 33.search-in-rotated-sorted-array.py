#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (33.94%)
# Likes:    4249
# Dislikes: 423
# Total Accepted:    642.2K
# Total Submissions: 1.9M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# 
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# Example 1:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# 
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        
        while l <= r:
            if target == nums[l]:
                return l
            if target == nums[r]:
                return r
            mid = (l+r)//2
            if l == mid:
                return -1
            
            if nums[mid] == target:
                return mid
            
            if nums[l] < nums[mid]:
                if target < nums[mid] and target > nums[l]:
                    l, r = l+1, mid-1
                else:
                    l, r = mid+1, r-1
            else:
                if target < nums[mid] or target > nums[l]:
                    l, r = l+1, mid-1
                else:
                    l, r = mid+1, r-1
        return -1
# @lc code=end

