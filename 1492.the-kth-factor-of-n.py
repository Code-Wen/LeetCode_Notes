#
# @lc app=leetcode id=1492 lang=python3
#
# [1492] The kth Factor of n
#
# https://leetcode.com/problems/the-kth-factor-of-n/description/
#
# algorithms
# Medium (70.80%)
# Likes:    54
# Dislikes: 16
# Total Accepted:    7.9K
# Total Submissions: 11.1K
# Testcase Example:  '12\n3'
#
# Given two positive integers n and k.
# 
# A factor of an integer n is defined as an integer i where n % i == 0.
# 
# Consider a list of all factors of n sorted in ascending order, return the kth
# factor in this list or return -1 if n has less than k factors.
# 
# 
# Example 1:
# 
# 
# Input: n = 12, k = 3
# Output: 3
# Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.
# 
# 
# Example 2:
# 
# 
# Input: n = 7, k = 2
# Output: 7
# Explanation: Factors list is [1, 7], the 2nd factor is 7.
# 
# 
# Example 3:
# 
# 
# Input: n = 4, k = 4
# Output: -1
# Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should
# return -1.
# 
# 
# Example 4:
# 
# 
# Input: n = 1, k = 1
# Output: 1
# Explanation: Factors list is [1], the 1st factor is 1.
# 
# 
# Example 5:
# 
# 
# Input: n = 1000, k = 3
# Output: 4
# Explanation: Factors list is [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125,
# 200, 250, 500, 1000].
# 
# 
# 
# Constraints:
# 
# 
# 1 <= k <= n <= 1000
# 
#

# @lc code=start
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, int(sqrt(n))+1):
            if n%i == 0:
                factors.append(i)
                if len(factors)==k: return factors[-1]
        isSquare = (n//factors[-1]) == factors[-1]
        nFactors = 2*len(factors) if not isSquare else 2*len(factors)-1
        if nFactors < k: return -1
        else:
            if isSquare:
                return n//factors[len(factors)-k-1]
            else:
                return n//factors[len(factors)-k]

# @lc code=end

