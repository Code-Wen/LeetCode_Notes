#
# @lc app=leetcode id=1437 lang=python3
#
# [1437] Check If All 1's Are at Least Length K Places Away
#
# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/description/
#
# algorithms
# Medium (68.25%)
# Likes:    18
# Dislikes: 2
# Total Accepted:    8.5K
# Total Submissions: 12.4K
# Testcase Example:  '[1,0,0,0,1,0,0,1]\r\n2\r'
#
# Given an array nums of 0s and 1s and an integer k, return True if all 1's are
# at least k places away from each other, otherwise return False.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: nums = [1,0,0,0,1,0,0,1], k = 2
# Output: true
# Explanation: Each of the 1s are at least 2 places away from each other.
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: nums = [1,0,0,1,0,1], k = 2
# Output: false
# Explanation: The second 1 and third 1 are only one apart from each other.
# 
# Example 3:
# 
# 
# Input: nums = [1,1,1,1,1], k = 0
# Output: true
# 
# 
# Example 4:
# 
# 
# Input: nums = [0,1,0,1], k = 1
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# 0 <= k <= nums.length
# nums[i] is 0 or 1
# 
#

# @lc code=start
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        gap = 0
        for i, n in enumerate(nums):
            if n==1 and i>0:
                if gap < k: return False
                else: gap = 0
            else:
                gap += 1
        return True
# @lc code=end

