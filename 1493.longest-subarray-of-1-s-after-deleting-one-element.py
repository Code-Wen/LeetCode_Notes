#
# @lc app=leetcode id=1493 lang=python3
#
# [1493] Longest Subarray of 1's After Deleting One Element
#
# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/
#
# algorithms
# Medium (57.80%)
# Likes:    137
# Dislikes: 3
# Total Accepted:    7.5K
# Total Submissions: 13K
# Testcase Example:  '[1,1,0,1]'
#
# Given a binary array nums, you should delete one element from it.
# 
# Return the size of the longest non-empty subarray containing only 1's in the
# resulting array.
# 
# Return 0 if there is no such subarray.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3
# numbers with value of 1's.
# 
# Example 2:
# 
# 
# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1]
# longest subarray with value of 1's is [1,1,1,1,1].
# 
# Example 3:
# 
# 
# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.
# 
# Example 4:
# 
# 
# Input: nums = [1,1,0,0,1,1,1,0,1]
# Output: 4
# 
# 
# Example 5:
# 
# 
# Input: nums = [0,0,0]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.
# 
# 
#

# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res, prevStreak, curStreak, deleted = 0, 0, 0, False
        for n in nums:
            if n == 1:
                curStreak += 1
                res = max(res, prevStreak+curStreak)
            else:
                deleted = 1
                prevStreak, curStreak = curStreak, 0
        return res if deleted else res-1

# @lc code=end

