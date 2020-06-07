#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#
# https://leetcode.com/problems/counting-bits/description/
#
# algorithms
# Medium (67.53%)
# Likes:    2423
# Dislikes: 152
# Total Accepted:    255.7K
# Total Submissions: 374.8K
# Testcase Example:  '2'
#
# Given a non negative integer number num. For every numbers i in the range 0 ≤
# i ≤ num calculate the number of 1's in their binary representation and return
# them as an array.
# 
# Example 1:
# 
# 
# Input: 2
# Output: [0,1,1]
# 
# Example 2:
# 
# 
# Input: 5
# Output: [0,1,1,2,1,2]
# 
# 
# Follow up:
# 
# 
# It is very easy to come up with a solution with run time
# O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a
# single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function like
# __builtin_popcount in c++ or in any other language.
# 
#

# @lc code=start
class Solution:
    def countBits(self, num: int) -> List[int]:
        # Building up the result list from previous results.
        L = num + 1
        res = [0]
        while len(res) < L:
            res += [i+1 for i in res[:min(L-len(res), len(res))]]
        return res
# @lc code=end

