#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#
# https://leetcode.com/problems/contains-duplicate-iii/description/
#
# algorithms
# Medium (20.93%)
# Likes:    1167
# Dislikes: 1259
# Total Accepted:    134.7K
# Total Submissions: 640.6K
# Testcase Example:  '[1,2,3,1]\n3\n0'
#
# Given an array of integers, find out whether there are two distinct indices i
# and j in the array such that the absolute difference between nums[i] and
# nums[j] is at most t and the absolute difference between i and j is at most
# k.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,0,1,1], k = 1, t = 2
# Output: true
# 
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,5,9,1,5,9], k = 2, t = 3
# Output: false
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0 or k == 0: return False
        # Keeping at most k buckets
        buckets, s = {}, t+1
        for i in range(len(nums)):
            key = nums[i]//s
            if key in buckets:
                return True
            if key - 1 in buckets and nums[i] - buckets[key-1] <= t:
                return True
            if key + 1 in buckets and buckets[key+1] - nums[i] <= t:
                return True
            buckets[key] = nums[i]
            if i >= k:
                del buckets[nums[i-k]//s]
        return False
# @lc code=end

