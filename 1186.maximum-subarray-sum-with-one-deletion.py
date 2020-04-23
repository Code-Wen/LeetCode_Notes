#
# @lc app=leetcode id=1186 lang=python3
#
# [1186] Maximum Subarray Sum with One Deletion
#
# https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/description/
#
# algorithms
# Medium (36.29%)
# Likes:    376
# Dislikes: 15
# Total Accepted:    11.9K
# Total Submissions: 32.8K
# Testcase Example:  '[1,-2,0,3]'
#
# Given an array of integers, return the maximum sum for a non-empty subarray
# (contiguous elements) with at most one element deletion. In other words, you
# want to choose a subarray and optionally delete one element from it so that
# there is still at least one element left and the sum of the remaining
# elements is maximum possible.
# 
# Note that the subarray needs to be non-empty after deleting one element.
# 
# 
# Example 1:
# 
# 
# Input: arr = [1,-2,0,3]
# Output: 4
# Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the
# subarray [1, 0, 3] becomes the maximum value.
# 
# Example 2:
# 
# 
# Input: arr = [1,-2,-2,3]
# Output: 3
# Explanation: We just choose [3] and it's the maximum sum.
# 
# 
# Example 3:
# 
# 
# Input: arr = [-1,-1,-1,-1]
# Output: -1
# Explanation: The final subarray needs to be non-empty. You can't choose [-1]
# and delete -1 from it, then get an empty subarray to make the sum equals to
# 0.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 10^5
# -10^4 <= arr[i] <= 10^4
# 
#

# @lc code=start
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1: return arr[0]

        bestPrefixSum, bestSuffixSum = [0]*n, [0]*n
        preMin, sufMin, preSum, sufSum  = 0,0,0,0
        for i in range(n):
            # Get the inclusive prefix/suffix sum
            preSum += arr[i]
            sufSum += arr[-i-1]
            # Update 
            bestPrefixSum[i] = preSum - preMin
            bestSuffixSum[-i-1] = sufSum - sufMin
            # Update minimal prefix/suffix sum we have seen so far
            preMin, sufMin = min(preMin, preSum), min(sufMin, sufSum)
        # Try deleting each element and search for best subarray
        # If arr[i] is deleted, then the best subarray sum by 
        # possibly pasting the left side and right side of i is 
        # max(bestPrefixSum[i-1] , bestSuffixSum[i+1], bestPrefixSum[i-1]+bestSuffixSum[i+1]])
        res = max(bestSuffixSum[1], bestPrefixSum[-2])
        for i in range(1, n-1):
            leftSum = bestPrefixSum[i-1] 
            rightSum = bestSuffixSum[i+1]
            res = max([leftSum, rightSum, leftSum+rightSum, res])
        return res



# @lc code=end

