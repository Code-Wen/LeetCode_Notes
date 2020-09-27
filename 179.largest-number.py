#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#
# https://leetcode.com/problems/largest-number/description/
#
# algorithms
# Medium (29.09%)
# Likes:    2333
# Dislikes: 260
# Total Accepted:    205.8K
# Total Submissions: 698.5K
# Testcase Example:  '[10,2]'
#
# Given a list of non negative integers, arrange them such that they form the
# largest number.
# 
# Example 1:
# 
# 
# Input: [10,2]
# Output: "210"
# 
# Example 2:
# 
# 
# Input: [3,30,34,5,9]
# Output: "9534330"
# 
# 
# Note: The result may be very large, so you need to return a string instead of
# an integer.
# 
#

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(n) for n in nums]
        for i in range(1, len(nums)):
            j = i - 1
            while j >= 0 and int(nums[j+1]+nums[j]) > int(nums[j]+nums[j+1]):
                nums[j+1], nums[j] = nums[j], nums[j+1]
                j -= 1
        res = ''.join(nums)
        return res if res[0]!='0' else '0'
# @lc code=end

