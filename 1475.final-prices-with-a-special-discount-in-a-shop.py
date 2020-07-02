#
# @lc app=leetcode id=1475 lang=python3
#
# [1475] Final Prices With a Special Discount in a Shop
#
# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/
#
# algorithms
# Easy (76.07%)
# Likes:    130
# Dislikes: 11
# Total Accepted:    12.7K
# Total Submissions: 16.7K
# Testcase Example:  '[8,4,6,2,3]'
#
# Given the array prices where prices[i] is the price of the ith item in a
# shop. There is a special discount for items in the shop, if you buy the ith
# item, then you will receive a discount equivalent to prices[j] where j is the
# minimum index such that j > i and prices[j] <= prices[i], otherwise, you will
# not receive any discount at all.
# 
# Return an array where the ith element is the final price you will pay for the
# ith item of the shop considering the special discount.
# 
# 
# Example 1:
# 
# 
# Input: prices = [8,4,6,2,3]
# Output: [4,2,4,2,3]
# Explanation: 
# For item 0 with price[0]=8 you will receive a discount equivalent to
# prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4. 
# For item 1 with price[1]=4 you will receive a discount equivalent to
# prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2. 
# For item 2 with price[2]=6 you will receive a discount equivalent to
# prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4. 
# For items 3 and 4 you will not receive any discount at all.
# 
# 
# Example 2:
# 
# 
# Input: prices = [1,2,3,4,5]
# Output: [1,2,3,4,5]
# Explanation: In this case, for all items, you will not receive any discount
# at all.
# 
# 
# Example 3:
# 
# 
# Input: prices = [10,1,1,6]
# Output: [9,0,1,6]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= prices.length <= 500
# 1 <= prices[i] <= 10^3
# 
# 
#

# @lc code=start
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res, L = prices.copy(), len(prices)
        discountIdx = [-1]*L
        for i in range(L-2, -1, -1):
            idx = i + 1
            while idx != -1 and prices[idx] > prices[i]:
                idx = discountIdx[idx]
            discountIdx[i] = idx
        for i in range(L):
            discount = discountIdx[i]
            if discount > 0:
                res[i] -= prices[discount]
        return res
# @lc code=end

