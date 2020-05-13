#
# @lc app=leetcode id=901 lang=python3
#
# [901] Online Stock Span
#
# https://leetcode.com/problems/online-stock-span/description/
#
# algorithms
# Medium (53.89%)
# Likes:    416
# Dislikes: 65
# Total Accepted:    20K
# Total Submissions: 37.1K
# Testcase Example:  '["StockSpanner","next","next","next","next","next","next","next"]\n' +
  '[[],[100],[80],[60],[70],[60],[75],[85]]'
#
# Write a class StockSpanner which collects daily price quotes for some stock,
# and returns the span of that stock's price for the current day.
# 
# The span of the stock's price today is defined as the maximum number of
# consecutive days (starting from today and going backwards) for which the
# price of the stock was less than or equal to today's price.
# 
# For example, if the price of a stock over the next 7 days were [100, 80, 60,
# 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: ["StockSpanner","next","next","next","next","next","next","next"],
# [[],[100],[80],[60],[70],[60],[75],[85]]
# Output: [null,1,1,1,2,1,4,6]
# Explanation: 
# First, S = StockSpanner() is initialized.  Then:
# S.next(100) is called and returns 1,
# S.next(80) is called and returns 1,
# S.next(60) is called and returns 1,
# S.next(70) is called and returns 2,
# S.next(60) is called and returns 1,
# S.next(75) is called and returns 4,
# S.next(85) is called and returns 6.
# 
# Note that (for example) S.next(75) returned 4, because the last 4 prices
# (including today's price of 75) were less than or equal to today's
# price.
# 
# 
# 
# 
# Note:
# 
# 
# Calls to StockSpanner.next(int price) will have 1 <= price <= 10^5.
# There will be at most 10000 calls to StockSpanner.next per test case.
# There will be at most 150000 calls to StockSpanner.next across all test
# cases.
# The total time limit for this problem has been reduced by 75% for C++, and
# 50% for all other languages.
# 
# 
# 
#

# @lc code=start
class StockSpanner:

    def __init__(self):
        # self.data[i] = (price_i, span_i)
        self.data = []
        self.maxQ = collections.deque()

    def next(self, price: int) -> int:
        idx, N = len(self.data), len(self.data)+1
        while self.maxQ and self.data[self.maxQ[-1]][0] <= price:
            idx = self.maxQ.pop()
        if len(self.maxQ)==0: 
            idx = 0
        self.maxQ.append(N-1)
        if idx == N-1:
            res = 1
        else:
            res = N - idx + self.data[idx][1]-1 if self.data else N-idx
        self.data.append((price, res))
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end

