#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
# https://leetcode.com/problems/sort-colors/description/
#
# algorithms
# Medium (45.56%)
# Likes:    3133
# Dislikes: 213
# Total Accepted:    476.2K
# Total Submissions: 1M
# Testcase Example:  '[2,0,2,1,1,0]'
#
# Given an array with n objects colored red, white or blue, sort them in-place
# so that objects of the same color are adjacent, with the colors in the order
# red, white and blue.
# 
# Here, we will use the integers 0, 1, and 2 to represent the color red, white,
# and blue respectively.
# 
# Note: You are not suppose to use the library's sort function for this
# problem.
# 
# Example:
# 
# 
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# 
# Follow up:
# 
# 
# A rather straight forward solution is a two-pass algorithm using counting
# sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite
# array with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?
# 
# 
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # ptrs[0], ptrs[1] are the indices for the next 0 and the next 1
        ptrs = [0, 0]
        for i in range(len(nums)):
            moveOne = False
            if nums[i] == 0:
                nums[i], nums[ptrs[0]] = nums[ptrs[0]], nums[i]
                ptrs[0] += 1
                moveOne = True # If we move ptrs[0], we have to move ptrs[1]
                
            if nums[i] == 1:
                nums[i], nums[ptrs[1]] = nums[ptrs[1]], nums[i]
                moveOne = True
            if moveOne: ptrs[1] += 1
# @lc code=end

