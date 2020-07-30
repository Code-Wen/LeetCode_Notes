#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
#
# algorithms
# Medium (46.25%)
# Likes:    2510
# Dislikes: 86
# Total Accepted:    146.7K
# Total Submissions: 313.8K
# Testcase Example:  '[1,2,3,0,2]'
#
# Say you have an array for which the i^th element is the price of a given
# stock on day i.
# 
# Design an algorithm to find the maximum profit. You may complete as many
# transactions as you like (ie, buy one and sell one share of the stock
# multiple times) with the following restrictions:
# 
# 
# You may not engage in multiple transactions at the same time (ie, you must
# sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1
# day)
# 
# 
# Example:
# 
# 
# Input: [1,2,3,0,2]
# Output: 3 
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        
        buy, sell = [0] * (len(prices)+2), [0] * (len(prices)+2)
        buy[1] = -prices[0]
        for i in range(2, len(buy)):
            buy[i] = max(sell[i-2]-prices[i-2], buy[i-1])
            sell[i] = max(buy[i-1]+prices[i-2], sell[i-1])
        return sell[-1]
# @lc code=end

