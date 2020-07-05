#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#
# https://leetcode.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (39.75%)
# Likes:    1764
# Dislikes: 112
# Total Accepted:    160.3K
# Total Submissions: 392.1K
# Testcase Example:  '10'
#
# Write a program to find the n-th ugly number.
# 
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
# 
# Example:
# 
# 
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10
# ugly numbers.
# 
# Note:  
# 
# 
# 1 is typically treated as an ugly number.
# n does not exceed 1690.
# 
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1]
        i2,i3,i5 = 0 ,0, 0
        while n > 1:
            u2, u3, u5 = dp[i2] * 2, dp[i3]*3, dp[i5]*5
            m = min(u2,u3,u5)
            dp.append(m)
            if m == u2:
                i2 += 1
            if m == u3:
                i3 += 1
            if m == u5:
                i5 += 1
            n -= 1
        return dp[-1]
# @lc code=end

