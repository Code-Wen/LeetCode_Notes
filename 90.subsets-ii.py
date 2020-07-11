#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (46.58%)
# Likes:    1636
# Dislikes: 69
# Total Accepted:    277.9K
# Total Submissions: 595K
# Testcase Example:  '[1,2,2]'
#
# Given a collection of integers that might contain duplicates, nums, return
# all possible subsets (the power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: [1,2,2]
# Output:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
# 
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, prev, count = [[]], float('inf'), 0
        nums.sort()
        for n in nums:
            if n == prev:
                res += [s+[n] for s in res if (len(s) >= count and s[-count] == n)]
                count += 1
            else:
                res += [s+[n] for s in res]
                prev = n
                count = 1
        return res
# @lc code=end

