#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (59.14%)
# Likes:    4090
# Dislikes: 352
# Total Accepted:    442.1K
# Total Submissions: 748.1K
# Testcase Example:  '[1,2,3,4]'
#
# Given an array nums of n integers where n > 1,  return an array output such
# that output[i] is equal to the product of all the elements of nums except
# nums[i].
# 
# Example:
# 
# 
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# 
# 
# Constraint: It's guaranteed that the product of the elements of any prefix or
# suffix of the array (including the whole array) fits in a 32 bit integer.
# 
# Note: Please solve it without division and in O(n).
# 
# Follow up:
# Could you solve it with constant space complexity? (The output array does not
# count as extra space for the purpose of space complexity analysis.)
# 
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res, prefixProd, suffixProd = [1] * n, 1, 1
        for i in range(1,n):
            prefixProd *= nums[i-1]
            res[i] = prefixProd
        
        for i in range(n-2, -1, -1):
            suffixProd *= nums[i+1]
            res[i] *= suffixProd
        return res
# @lc code=end

