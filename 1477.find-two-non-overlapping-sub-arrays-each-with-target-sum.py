#
# @lc app=leetcode id=1477 lang=python3
#
# [1477] Find Two Non-overlapping Sub-arrays Each With Target Sum
#
# https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/description/
#
# algorithms
# Medium (27.21%)
# Likes:    282
# Dislikes: 14
# Total Accepted:    6.3K
# Total Submissions: 23.2K
# Testcase Example:  '[3,2,2,4,3]\n3'
#
# Given an array of integers arr and an integer target.
# 
# You have to find two non-overlapping sub-arrays of arr each with sum equal
# target. There can be multiple answers so you have to find an answer where the
# sum of the lengths of the two sub-arrays is minimum.
# 
# Return the minimum sum of the lengths of the two required sub-arrays, or
# return -1 if you cannot find such two sub-arrays.
# 
# 
# Example 1:
# 
# 
# Input: arr = [3,2,2,4,3], target = 3
# Output: 2
# Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their
# lengths is 2.
# 
# 
# Example 2:
# 
# 
# Input: arr = [7,3,4,7], target = 7
# Output: 2
# Explanation: Although we have three non-overlapping sub-arrays of sum = 7
# ([7], [3,4] and [7]), but we will choose the first and third sub-arrays as
# the sum of their lengths is 2.
# 
# 
# Example 3:
# 
# 
# Input: arr = [4,3,2,6,2,3,4], target = 6
# Output: -1
# Explanation: We have only one sub-array of sum = 6.
# 
# 
# Example 4:
# 
# 
# Input: arr = [5,5,4,4,5], target = 3
# Output: -1
# Explanation: We cannot find a sub-array of sum = 3.
# 
# 
# Example 5:
# 
# 
# Input: arr = [3,1,1,1,5,1,2,1], target = 3
# Output: 3
# Explanation: Note that sub-arrays [1,2] and [2,1] cannot be an answer because
# they overlap.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 10^5
# 1 <= arr[i] <= 1000
# 1 <= target <= 10^8
# 
# 
#

# @lc code=start
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        pairs = self.slidingWindow(arr, target)
        if not pairs or pairs[0][1] >= pairs[-1][0]: return -1

        leftMin, rightMin = [float('inf')]*len(arr), [float('inf')]*len(arr)
        for l, r in pairs:
            if r < len(arr)-1:
                leftMin[r+1] = min(leftMin[r+1], r-l+1)
        for l,r in pairs[::-1]:
            rightMin[l] = min(rightMin[l], r-l+1)
        for i in range(1,len(arr)):
            leftMin[i] = min(leftMin[i], leftMin[i-1])
            rightMin[-i-1] = min(rightMin[-i], rightMin[-i-1])
        return min([leftMin[i]+rightMin[i] for i in range(len(arr))])


    def slidingWindow(self, arr, target):
        """
        Find all the pairs (l,r) such that sum(arr[l:r+1]) == target
        """
        l, r, runningSum, res = 0, 0, arr[0], []
        while r < len(arr):
            
            while runningSum > target:
                runningSum -= arr[l]
                l += 1
            if runningSum == target:
                res.append((l,r))
                runningSum -= arr[l]
                l += 1
            
            else:
                r += 1
                if r < len(arr): runningSum += arr[r]
            if l > r: 
                r = l
                if r < len(arr):
                    runningSum += arr[r]
            
        return res
                
# @lc code=end

