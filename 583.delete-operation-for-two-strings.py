#
# @lc app=leetcode id=583 lang=python3
#
# [583] Delete Operation for Two Strings
#
# https://leetcode.com/problems/delete-operation-for-two-strings/description/
#
# algorithms
# Medium (48.66%)
# Likes:    1140
# Dislikes: 26
# Total Accepted:    52.1K
# Total Submissions: 106.8K
# Testcase Example:  '"sea"\n"eat"'
#
# 
# Given two words word1 and word2, find the minimum number of steps required to
# make word1 and word2 the same, where in each step you can delete one
# character in either string.
# 
# 
# Example 1:
# 
# Input: "sea", "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make
# "eat" to "ea".
# 
# 
# 
# Note:
# 
# The length of given words won't exceed 500.
# Characters in given words can only be lower-case letters.
# 
# 
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Use a 2-dim dp to find the longest common substrings of word1 and word2
        m, n = len(word1), len(word2)
        dp = [[0]* (n+1) for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    continue
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return m + n - 2*dp[-1][-1]
# @lc code=end

