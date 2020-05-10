#
# @lc app=leetcode id=954 lang=python3
#
# [954] Array of Doubled Pairs
#
# https://leetcode.com/problems/array-of-doubled-pairs/description/
#
# algorithms
# Medium (35.36%)
# Likes:    225
# Dislikes: 45
# Total Accepted:    16.4K
# Total Submissions: 46.4K
# Testcase Example:  '[3,1,3,6]'
#
# Given an array of integers A with even length, return true if and only if it
# is possible to reorder it such that A[2 * i + 1] = 2 * A[2 * i] for every 0
# <= i < len(A) / 2.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [3,1,3,6]
# Output: false
# 
# 
# 
# Example 2:
# 
# 
# Input: [2,1,2,6]
# Output: false
# 
# 
# 
# Example 3:
# 
# 
# Input: [4,-2,2,-4]
# Output: true
# Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or
# [2,4,-2,-4].
# 
# 
# 
# Example 4:
# 
# 
# Input: [1,2,4,16,8,4]
# Output: false
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= A.length <= 30000
# A.length is even
# -100000 <= A[i] <= 100000
# 
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        counts = collections.Counter(A)
        neg = sorted([n for n in counts.keys() if n<0])
        pos = sorted([n for n in counts.keys() if n>0])[::-1]
        if 0 in counts and counts[0]%2: return False
        while neg:
            n = neg.pop()
            if counts[n] == 0: continue
            if 2*n not in counts or counts[2*n]< counts[n]:
                return False
            else:
                counts[2*n] -= counts[n]
        while pos:
            n = pos.pop()
            if counts[n] == 0: continue
            if 2*n not in counts or counts[2*n]< counts[n]:
                return False
            else:
                counts[2*n] -= counts[n]
        return True
        


# @lc code=end

