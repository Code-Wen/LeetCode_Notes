#
# @lc app=leetcode id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/
#
# algorithms
# Medium (48.73%)
# Likes:    1022
# Dislikes: 44
# Total Accepted:    53.9K
# Total Submissions: 110.7K
# Testcase Example:  '[1,2,3,2,1]\n[3,2,1,4,7]'
#
# Given two integer arrays A and B, return the maximum length of an subarray
# that appears in both arrays.
# 
# Example 1:
# 
# 
# Input:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# Output: 3
# Explanation: 
# The repeated subarray with maximum length is [3, 2, 1].
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        m,n = len(A)+1, len(B)+1
        if m * n == 1: return 0

        dp, res = [[0]*n for _ in range(m)], 0
        for i in range(1,m):
            for j in range(1,n):
                if A[i-1] == B[j-1]:
                    temp = dp[i][j] = dp[i-1][j-1] + 1
                    res = max(res,temp)
        return res


# @lc code=end

