#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (56.52%)
# Likes:    2830
# Dislikes: 212
# Total Accepted:    577.9K
# Total Submissions: 1M
# Testcase Example:  '[3,2,3]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
# 
# You may assume that the array is non-empty and the majority element always
# exist in the array.
# 
# Example 1:
# 
# 
# Input: [3,2,3]
# Output: 3
# 
# Example 2:
# 
# 
# Input: [2,2,1,1,1,2,2]
# Output: 2
# 
# 
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        net, res = 1, nums[0]
        for n in nums[1:]:
            if net == 0:
                net, res = 1, n
            elif res == n:
                net += 1
            else:
                net -= 1
        return res
# @lc code=end

