#
# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#
# https://leetcode.com/problems/largest-divisible-subset/description/
#
# algorithms
# Medium (36.33%)
# Likes:    1248
# Dislikes: 60
# Total Accepted:    87.9K
# Total Submissions: 232K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct positive integers, find the largest subset such that
# every pair (Si, Sj) of elements in this subset satisfies:
# 
# Si % Sj = 0 or Sj % Si = 0.
# 
# If there are multiple solutions, return any subset is fine.
# 
# Example 1:
# 
# 
# 
# Input: [1,2,3]
# Output: [1,2] (of course, [1,3] will also be ok)
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,2,4,8]
# Output: [1,2,4,8]
# 
# 
# 
#

# @lc code=start
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) < 2: return nums
        nums.sort()
        dp, res = [[i] for i in nums], []
        for i in range(1,len(nums)):
            temp = dp[i]
            for j in range(i):
                if nums[i]%nums[j] == 0 and len(dp[j])+1 > len(temp):
                    temp = dp[j] + [nums[i]]
            dp[i] = temp
            if len(res) < len(temp):
                res = temp
        return res


# @lc code=end

