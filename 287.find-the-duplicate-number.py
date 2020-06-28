#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#
# https://leetcode.com/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (53.83%)
# Likes:    4507
# Dislikes: 554
# Total Accepted:    326.2K
# Total Submissions: 598.4K
# Testcase Example:  '[1,3,4,2,2]'
#
# Given an array nums containing n + 1 integers where each integer is between 1
# and n (inclusive), prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.
# 
# Example 1:
# 
# 
# Input: [1,3,4,2,2]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [3,1,3,4,2]
# Output: 3
# 
# Note:
# 
# 
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n^2).
# There is only one duplicate number in the array, but it could be repeated
# more than once.
# 
# 
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Some non-optimal solutions: 
        1. Sort then find duplicate adjacent numbers;
        2. Use hash tables

        Optimal solution: Floyd's Tortoise and Hare algorithm. 
        First detect the cycle, then find the entry of the cycle which is the duplicate.
        """
        slow=nums[0]
        fast=nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        fast=0
        while slow != fast:
            fast = nums[fast]
            slow = nums[slow]
        return slow
        
# @lc code=end

