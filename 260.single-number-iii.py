#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#
# https://leetcode.com/problems/single-number-iii/description/
#
# algorithms
# Medium (60.94%)
# Likes:    1610
# Dislikes: 105
# Total Accepted:    157.1K
# Total Submissions: 248.5K
# Testcase Example:  '[1,2,1,3,2,5]'
#
# Given an array of numbers nums, in which exactly two elements appear only
# once and all the other elements appear exactly twice. Find the two elements
# that appear only once.
# 
# Example:
# 
# 
# Input:  [1,2,1,3,2,5]
# Output: [3,5]
# 
# Note:
# 
# 
# The order of the result is not important. So in the above example, [5, 3] is
# also correct.
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant space complexity?
# 
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        bitmask = 0
        for n in nums:
            bitmask ^= n
        
        # find the right most bit where x and y are different
        rightDiff = bitmask & (-bitmask)
        
        x = 0
        for n in nums:
            if n & rightDiff:
                x ^= n
        return [x, bitmask^x]
# @lc code=end

