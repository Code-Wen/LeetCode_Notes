#
# @lc app=leetcode id=727 lang=python3
#
# [727] Minimum Window Subsequence
#
# https://leetcode.com/problems/minimum-window-subsequence/description/
#
# algorithms
# Hard (41.86%)
# Likes:    704
# Dislikes: 39
# Total Accepted:    41.8K
# Total Submissions: 99.9K
# Testcase Example:  '"abcdebdde"\n"bde"'
#
# Given strings S and T, find the minimum (contiguous) substring W of S, so
# that T is a subsequence of W.
# 
# If there is no such window in S that covers all characters in T, return the
# empty string "". If there are multiple such minimum-length windows, return
# the one with the left-most starting index.
# 
# Example 1:
# 
# 
# Input: 
# S = "abcdebdde", T = "bde"
# Output: "bcde"
# Explanation: 
# "bcde" is the answer because it occurs before "bdde" which has the same
# length.
# "deb" is not a smaller window because the elements of T in the window must
# occur in order.
# 
# 
# 
# 
# Note:
# 
# 
# All the strings in the input will only contain lowercase letters.
# The length of S will be in the range [1, 20000].
# The length of T will be in the range [1, 100].
# 
# 
# 
#

# @lc code=start
class Solution:
    def minWindow(self, S: str, T: str) -> str:
        m, n = len(S), len(T)
        table = collections.defaultdict(list)
        
        for i, c in enumerate(T):
            table[c].append(i)
        
        length, start_pos = m+1, -1
        dp = [-1]*n
        
        for pos,c in enumerate(S):
            if c in table:
                for i in table[c][::-1]:
                    # If first letter of T, start over a new search
                    if i == 0:
                        dp[0] = pos
                    # If other letters of T, pass the position of the previous letter
                    else:
                        dp[i] = dp[i-1]
                    
                    # Update only if we reach the last letter of T with shorter length
                    if i == n-1 and dp[i] >= 0 and pos - dp[i] + 1 < length:
                        start_pos = dp[i]
                        length = pos - dp[i] + 1
                        
        if dp[-1] < 0: return ''
        return S[start_pos:start_pos+length]
                        
# @lc code=end

