#
# @lc app=leetcode id=659 lang=python3
#
# [659] Split Array into Consecutive Subsequences
#
# https://leetcode.com/problems/split-array-into-consecutive-subsequences/description/
#
# algorithms
# Medium (43.73%)
# Likes:    1242
# Dislikes: 413
# Total Accepted:    48.6K
# Total Submissions: 110.9K
# Testcase Example:  '[1,2,3,3,4,5]'
#
# Given an array nums sorted in ascending order, return true if and only if you
# can split it into 1 or more subsequences such that each subsequence consists
# of consecutive integers and has length at least 3.
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,3,3,4,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences : 
# 1, 2, 3
# 3, 4, 5
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3,3,4,4,5,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences : 
# 1, 2, 3, 4, 5
# 3, 4, 5
# 
# 
# 
# Example 3:
# 
# 
# Input: [1,2,3,4,4,5]
# Output: False
# 
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10000
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
# @lc code=end

