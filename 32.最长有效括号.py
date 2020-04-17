#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#
# https://leetcode-cn.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (30.06%)
# Likes:    587
# Dislikes: 0
# Total Accepted:    50.6K
# Total Submissions: 168.3K
# Testcase Example:  '"(()"'
#
# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
# 
# 示例 1:
# 
# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
# 
# 
# 示例 2:
# 
# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
# 
# 
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 1. Here we only consider CONTINUOUS substrings;
        # 2. dp[i+1] = length of longest valid substring ending in i-th position.

        dp, stack = [0]*(len(s)+1), []
        for i in range(len(s)):   
            if s[i] == "(":
                stack.append(i)
            else:
                if stack:
                    p = stack.pop()
                    dp[i+1] = dp[p]+i+1-p
        return max(dp)




        

# @lc code=end

