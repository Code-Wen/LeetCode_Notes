#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (45.74%)
# Likes:    2825
# Dislikes: 181
# Total Accepted:    297.5K
# Total Submissions: 637.7K
# Testcase Example:  '12'
#
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
# 
# Example 1:
# 
# 
# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
# 
# Example 2:
# 
# 
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        """
        A BFS solution.
        """
        squares, seen = set(), set()
        i = 1
        while True:
            square = i*i
            if square <= n:
                squares.add(square)
                seen.add(square)
                i += 1
            else:
                break
        cur, res = {x for x in squares}, 1
        while n not in seen:
            res += 1
            nxt = set()
            for i in squares:
                for j in cur:
                    k = i + j
                    if k not in seen and k<=n:
                        seen.add(k)
                        nxt.add(k)
            cur = nxt
        return res
# @lc code=end

