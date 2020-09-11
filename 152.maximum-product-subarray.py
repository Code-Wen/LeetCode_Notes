#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (31.73%)
# Likes:    4853
# Dislikes: 172
# Total Accepted:    373.3K
# Total Submissions: 1.2M
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.
# 
# Example 1:
# 
# 
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# 
# 
# Example 2:
# 
# 
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
# 
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # 1. Use zeros to divide the array
        # 2. For a subarray without zeros, either the entire product > 0,
        # or we need to go through the negative elements, and compare
        # the prefix product and the tail product
        if not nums: return float('-inf')
        
        zero_loc = [i for i in range(len(nums)) if nums[i] == 0]
        
        def helper(start, end):
            """
            Check maxProduct(nums[start:end]) assuming every number is non-zero.
            """
            if end - start == 1:
                return nums[start]
            if end == start:
                return 0
            
            prefixProd = [nums[start]]*(end-start)
            for i in range(1, end-start):
                prefixProd[i] = prefixProd[i-1]*nums[i+start]
            if prefixProd[-1] > 0:
                return prefixProd[-1]
            res = max(prefixProd)
            for i in range(end-start):
                if nums[i+start] < 0:
                    res = max(res, prefixProd[-1]//prefixProd[i])
            return res
        
        if not zero_loc:
            return helper(0, len(nums))
        
        res = max([0, helper(0, zero_loc[0]), helper(zero_loc[-1]+1, len(nums))])
        for i in range(1, len(zero_loc)):
            res = max(res, helper(zero_loc[i-1]+1, zero_loc[i]))
        return res
# @lc code=end

