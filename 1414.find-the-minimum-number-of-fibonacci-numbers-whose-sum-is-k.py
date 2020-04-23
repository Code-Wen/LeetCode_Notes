#
# @lc app=leetcode id=1414 lang=python3
#
# [1414] Find the Minimum Number of Fibonacci Numbers Whose Sum Is K
#
# https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/description/
#
# algorithms
# Medium (55.74%)
# Likes:    33
# Dislikes: 7
# Total Accepted:    4.4K
# Total Submissions: 8K
# Testcase Example:  '7'
#
# Given the number k, return the minimum number of Fibonacci numbers whose sum
# is equal to k, whether a Fibonacci number could be used multiple times.
# 
# The Fibonacci numbers are defined as:
# 
# 
# F1 = 1
# F2 = 1
# Fn = Fn-1 + Fn-2 , for n > 2.
# 
# It is guaranteed that for the given constraints we can always find such
# fibonacci numbers that sum k.
# 
# Example 1:
# 
# 
# Input: k = 7
# Output: 2 
# Explanation: The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ... 
# For k = 7 we can use 2 + 5 = 7.
# 
# Example 2:
# 
# 
# Input: k = 10
# Output: 2 
# Explanation: For k = 10 we can use 2 + 8 = 10.
# 
# 
# Example 3:
# 
# 
# Input: k = 19
# Output: 3 
# Explanation: For k = 19 we can use 1 + 5 + 13 = 19.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= k <= 10^9
# 
#

# @lc code=start
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:

        # Proof:
        # 1. In the best solution for k, no two adjacent fibonacci numbers: F(i)+F(i+1) = F(i+2).
        # 2. In the best solution, no duplicates: 2F(i) = F(i-1)+F(i+1).
        # 3. In the best solution, we must take the largest F(i) with F(i) <= k.
        # F(1)+F(3)+...+F(2i-1) = F(2i)-1, F(2)+...+F(2i)= F(2i+1)-1.

        # Recursive solution:
        # if k < 2: return k
        # a, b = 1, 1
        # while b <= k:
        #     a, b = b, a+b
        # return self.findMinFibonacciNumbers(k-a)+1

        # Iterative solution:
        res, a, b = 0, 1, 1
        while b <= k:
            a, b = b, a+b
        while k > 0:
            if k >= a:
                res += 1
                k -= a
            a, b = b-a, a
        return res



        
# @lc code=end

