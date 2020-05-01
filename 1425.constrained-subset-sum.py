#
# @lc app=leetcode id=1425 lang=python3
#
# [1425] Constrained Subset Sum
#
# https://leetcode.com/problems/constrained-subset-sum/description/
#
# algorithms
# Hard (40.89%)
# Likes:    146
# Dislikes: 9
# Total Accepted:    4K
# Total Submissions: 9.9K
# Testcase Example:  '[10,2,-10,5,20]\n2'
#
# Given an integer array nums and an integer k, return the maximum sum of a
# non-empty subset of that array such that for every two consecutive integers
# in the subset, nums[i] and nums[j], where i < j, the condition j - i <= k is
# satisfied.
# 
# A subset of an array is obtained by deleting some number of elements (can be
# zero) from the array, leaving the remaining elements in their original
# order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [10,2,-10,5,20], k = 2
# Output: 37
# Explanation: The subset is [10, 2, 5, 20].
# 
# 
# Example 2:
# 
# 
# Input: nums = [-1,-2,-3], k = 1
# Output: -1
# Explanation: The subset must be non-empty, so we choose the largest number.
# 
# 
# Example 3:
# 
# 
# Input: nums = [10,-2,-10,-5,20], k = 2
# Output: 23
# Explanation: The subset is [10, -2, -5, 20].
# 
# 
# 
# Constraints:
# 
# 
# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        # A typical DP problem.
        # dp[i] = the max sum of contrained subset whose last index is i
        # Thus dp[i] = nums[i] + max(max(dp[i-k:i]), 0)
        # In order to find max(dp[i-k:i]), we introduce a deque q
        # q keeps the indices of the maximal value in dp[i-k:i]
        # See https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
        # Method 3 for a detailed explanation.
        dp, q, res = nums.copy(), collections.deque([0]), nums[0]
        for i in range(1,k):
            dp[i] += max(res, 0) 
            # update q
            while q and dp[i] >= dp[q[-1]]:
                q.pop()
            q.append(i)
            # update res
            res = max(res, dp[i])
                
        for i in range(k, len(nums)):
            while q and q[0] < i-k:
                q.popleft()
            dp[i] += max(dp[q[0]],0)
            while q and dp[i] >= dp[q[-1]]:
                q.pop()
            q.append(i)
            res = max(res, dp[i])
        return res
# @lc code=end

