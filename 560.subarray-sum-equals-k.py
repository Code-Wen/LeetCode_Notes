#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
# https://leetcode.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (43.54%)
# Likes:    3821
# Dislikes: 124
# Total Accepted:    242.1K
# Total Submissions: 552.9K
# Testcase Example:  '[1,1,1]\n2'
#
# Given an array of integers and an integer k, you need to find the total
# number of continuous subarrays whose sum equals to k.
# 
# Example 1:
# 
# Input:nums = [1,1,1], k = 2
# Output: 2
# 
# 
# 
# Note:
# 
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the
# integer k is [-1e7, 1e7].
# 
# 
# 
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSum, prefixSums, res = 0, collections.defaultdict(int), 0
        for n in nums:
            preSum += n
            res += prefixSums[preSum - k]
            prefixSums[preSum] += 1
        return res+prefixSums[k]
# @lc code=end

