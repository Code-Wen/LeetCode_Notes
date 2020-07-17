#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
# https://leetcode.com/problems/powx-n/description/
#
# algorithms
# Medium (29.61%)
# Likes:    1559
# Dislikes: 3079
# Total Accepted:    488.5K
# Total Submissions: 1.6M
# Testcase Example:  '2.00000\n10'
#
# Implement pow(x, n), which calculates x raised to the power n (x^n).
# 
# Example 1:
# 
# 
# Input: 2.00000, 10
# Output: 1024.00000
# 
# 
# Example 2:
# 
# 
# Input: 2.10000, 3
# Output: 9.26100
# 
# 
# Example 3:
# 
# 
# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
# 
# 
# Note:
# 
# 
# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
# 
# 
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 and n != 0: return 0
        
        sign = -1 if n<0 else 1
        n, res, preComputed = abs(n), 1, {1:x}
        p = 1
        while 2*p <= n:
            preComputed[2*p] = preComputed[p]*preComputed[p]
            p *= 2
        while n > 0:
            for p in sorted(preComputed.keys())[::-1]:
                if p <= n:
                    res *= preComputed[p]
                    n -= p
                
                    
        
        return 1/res if sign < 0 else res
# @lc code=end

