#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#
# https://leetcode.com/problems/majority-element-ii/description/
#
# algorithms
# Medium (35.91%)
# Likes:    1931
# Dislikes: 178
# Total Accepted:    161.4K
# Total Submissions: 439.4K
# Testcase Example:  '[3,2,3]'
#
# Given an integer array of size n, find all elements that appear more than ⌊
# n/3 ⌋ times.
# 
# Note: The algorithm should run in linear time and in O(1) space.
# 
# Example 1:
# 
# 
# Input: [3,2,3]
# Output: [3]
# 
# Example 2:
# 
# 
# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]
# 
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1, cand2, cnt1, cnt2 = 0,1,0,0
        for n in nums:
            if n==cand1: cnt1 += 1
            elif n==cand2: cnt2 += 1
            elif cnt1==0: cand1, cnt1 = n, 1
            elif cnt2==0: cand2, cnt2 = n, 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        return [x for x in (cand1,cand2) if nums.count(x) > len(nums)//3]
# @lc code=end

