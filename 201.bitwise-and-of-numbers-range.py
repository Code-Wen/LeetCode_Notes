#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#
# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/
#
# algorithms
# Medium (37.24%)
# Likes:    772
# Dislikes: 100
# Total Accepted:    119.8K
# Total Submissions: 315.9K
# Testcase Example:  '5\n7'
#
# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND
# of all numbers in this range, inclusive.
# 
# Example 1:
# 
# 
# Input: [5,7]
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: [0,1]
# Output: 0
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # Trivial case
        if len(bin(n)) > len(bin(m)): return 0
        m_bin, n_bin = bin(m), bin(n)
        i = 2
        # Find the first occurrance of '1' in the binary rep of n 
        # where the corresponding letter is '0' in the binary rep of m
        while i<len(m_bin):
            if m_bin[i] == '0' and n_bin[i]=='1':
                break
            i += 1
        res_bin = m_bin[:i]+'0' * (len(m_bin) - i)
        return int(res_bin,2)
            
# @lc code=end

