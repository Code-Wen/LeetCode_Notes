#
# @lc app=leetcode id=548 lang=python3
#
# [548] Split Array with Equal Sum
#
# https://leetcode.com/problems/split-array-with-equal-sum/description/
#
# algorithms
# Medium (46.46%)
# Likes:    239
# Dislikes: 72
# Total Accepted:    13.9K
# Total Submissions: 29.6K
# Testcase Example:  '[1,2,1,2,1,2,1]'
#
# 
# Given an array with n integers, you need to find if there are triplets  (i,
# j, k) which satisfies following conditions:
# 
# ⁠0 < i, i + 1 < j, j + 1 < k < n - 1 
# ⁠Sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n -
# 1) should be equal. 
# 
# where we define that subarray (L, R) represents a slice of the original array
# starting from the element indexed L to the element indexed R.
# 
# 
# Example:
# 
# Input: [1,2,1,2,1,2,1]
# Output: True
# Explanation:
# i = 1, j = 3, k = 5. 
# sum(0, i - 1) = sum(0, 0) = 1
# sum(i + 1, j - 1) = sum(2, 2) = 1
# sum(j + 1, k - 1) = sum(4, 4) = 1
# sum(k + 1, n - 1) = sum(6, 6) = 1
# 
# 
# 
# Note:
# 
# ⁠1 
# ⁠Elements in the given array will be in range [-1,000,000, 1,000,000]. 
# 
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        # Ideas: 1. use prefix sum; 2. Choose mid index first
        # Time: O(n^2), Space: O(n)
        
        n = len(nums)
        # Not enough space to split
        if n < 7: return False
        
        prefixSum = [0]*n
        prefixSum[0] = nums[0]
        for i in range(1, n):
            # prefixSum[i] = sum(nums[:i+1])
            prefixSum[i] = prefixSum[i-1] + nums[i]
        
        # Choose mid index first
        for j in range(3, n-3):
            left, right = set(), set()
            for i in range(1, j-1):
                if prefixSum[i-1] == prefixSum[j-1] - prefixSum[i]:
                    left.add(prefixSum[i-1])
            if not left:
                continue
            for k in range(j+2, n-1):
                if prefixSum[k-1] - prefixSum[j] == prefixSum[-1] - prefixSum[k]:
                    right.add(prefixSum[k-1] - prefixSum[j])
            if len(left.intersection(right)) > 0:
                return True
        return False
# @lc code=end

