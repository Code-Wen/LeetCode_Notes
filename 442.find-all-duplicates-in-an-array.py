#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#
# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
#
# algorithms
# Medium (65.63%)
# Likes:    2433
# Dislikes: 153
# Total Accepted:    189.8K
# Total Submissions: 283.1K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements
# appear twice and others appear once.
# 
# Find all the elements that appear twice in this array.
# 
# Could you do it without extra space and in O(n) runtime?
# 
# Example:
# 
# Input:
# [4,3,2,7,8,2,3,1]
# 
# Output:
# [2,3]
# 
#

# @lc code=start
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        len(nums) = n and 1<=nums[i]<=n
        For any n in nums, we can negate nums[abs(n)-1]
        to indicate that we have seen n.
        """
        res = []
        for n in nums:
            loc = abs(n)-1
            if nums[loc]<0:
                res.append(abs(n))
            nums[loc] *= -1
        return res
# @lc code=end

