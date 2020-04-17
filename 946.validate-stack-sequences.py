#
# @lc app=leetcode id=946 lang=python3
#
# [946] Validate Stack Sequences
#
# https://leetcode.com/problems/validate-stack-sequences/description/
#
# algorithms
# Medium (59.42%)
# Likes:    564
# Dislikes: 18
# Total Accepted:    31.7K
# Total Submissions: 53.2K
# Testcase Example:  '[1,2,3,4,5]\n[4,5,3,2,1]'
#
# Given two sequences pushed and popped with distinct values, return true if
# and only if this could have been the result of a sequence of push and pop
# operations on an initially empty stack.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
# 
# 
# 
# Example 2:
# 
# 
# Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# Output: false
# Explanation: 1 cannot be popped before 2.
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= pushed.length == popped.length <= 1000
# 0 <= pushed[i], popped[i] < 1000
# pushed is a permutation of popped.
# pushed and popped have distinct values.
# 
# 
# 
#

# @lc code=start
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        d = {pushed[i]:i for i in range(len(pushed))}
        records, rightmost = [], -1
        for n in popped:
            idx = d[n]
            if rightmost < idx:
                cnt, rightmost = idx-rightmost, idx
                records.append([idx-1,cnt-1])
            else:
                if idx != records[-1][0]:
                    return False
                records[-1][0] -= 1
                records[-1][1] -= 1
            if records and records[-1][1] == 0:
                records.pop()
        return True
# @lc code=end

