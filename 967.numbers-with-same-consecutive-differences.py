#
# @lc app=leetcode id=967 lang=python3
#
# [967] Numbers With Same Consecutive Differences
#
# https://leetcode.com/problems/numbers-with-same-consecutive-differences/description/
#
# algorithms
# Medium (39.43%)
# Likes:    350
# Dislikes: 87
# Total Accepted:    24.6K
# Total Submissions: 58.5K
# Testcase Example:  '3\n7'
#
# Return all non-negative integers of length N such that the absolute
# difference between every two consecutive digits is K.
# 
# Note that every number in the answer must not have leading zeros except for
# the number 0 itself. For example, 01 has one leading zero and is invalid, but
# 0 is valid.
# 
# You may return the answer in any order.
# 
# 
# 
# Example 1:
# 
# 
# Input: N = 3, K = 7
# Output: [181,292,707,818,929]
# Explanation: Note that 070 is not a valid number, because it has leading
# zeroes.
# 
# 
# 
# Example 2:
# 
# 
# Input: N = 2, K = 1
# Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 9
# 0 <= K <= 9
# 
# 
#

# @lc code=start
class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N == 1: return [i for i in range(10)]
        d = {}
        for i in range(10):
            choices = set()
            if i >= K:
                choices.add(str(i-K))
            if i+K < 10:
                choices.add(str(i+K))
            if choices:
                d[str(i)] = choices
            
        res, l = [s for s in d.keys() if s!='0'], 1
        while l < N:
            res = [s+t for s in res for t in d[s[-1]]]
            l += 1
        return [int(s) for s in res]
# @lc code=end

