# 562. Longest Line of Consecutive One in Matrix
# Medium
#https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/

# Share
# Given a 01 matrix M, find the longest line of consecutive one in the matrix. The line could be horizontal, vertical, diagonal or anti-diagonal.
# Example:
# Input:
# [[0,1,1,0],
#  [0,1,1,0],
#  [0,0,0,1]]
# Output: 3
# Hint: The number of elements in the given matrix will not exceed 10,000.

class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        if not M or not M[0]: return 0
        m, n = len(M), len(M[0]) 
        # dp[i][j] is list of length 4: horizontal, vertical, diagonal, anti-diagonal
        dp = [[[0]*4 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if M[i][j] == 0: continue
                else:
                    dp[i][j][0] = 1 + dp[i][j-1][0] if j > 0 else 1
                    dp[i][j][1] = 1 + dp[i-1][j][1] if i > 0 else 1
                    dp[i][j][2] = 1 + dp[i-1][j-1][2] if j > 0 and i > 0 else 1
                    dp[i][j][3] = 1 + dp[i-1][j+1][3] if j+1 < n and i >0 else 1
        return max([max([max(x) for x in row]) for row in dp])                  
                    