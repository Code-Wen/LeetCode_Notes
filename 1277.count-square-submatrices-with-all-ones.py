#
# @lc app=leetcode id=1277 lang=python3
#
# [1277] Count Square Submatrices with All Ones
#
# https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/
#
# algorithms
# Medium (69.17%)
# Likes:    624
# Dislikes: 15
# Total Accepted:    33.9K
# Total Submissions: 47.3K
# Testcase Example:  '[[0,1,1,1],[1,1,1,1],[0,1,1,1]]'
#
# Given a m * n matrix of ones and zeros, return how many square submatrices
# have all ones.
# 
# 
# Example 1:
# 
# 
# Input: matrix =
# [
# [0,1,1,1],
# [1,1,1,1],
# [0,1,1,1]
# ]
# Output: 15
# Explanation: 
# There are 10 squares of side 1.
# There are 4 squares of side 2.
# There is  1 square of side 3.
# Total number of squares = 10 + 4 + 1 = 15.
# 
# 
# Example 2:
# 
# 
# Input: matrix = 
# [
# ⁠ [1,0,1],
# ⁠ [1,1,0],
# ⁠ [1,1,0]
# ]
# Output: 7
# Explanation: 
# There are 6 squares of side 1.  
# There is 1 square of side 2. 
# Total number of squares = 6 + 1 = 7.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 300
# 1 <= arr[0].length <= 300
# 0 <= arr[i][j] <= 1
# 
# 
#

# @lc code=start
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # dp[i][j] = maximal size of square with top-left corner at (i,j)
        m, n = len(matrix), len(matrix[0])
        dp = copy.deepcopy(matrix)
        
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                if matrix[i][j]:
                    dp[i][j] = 1 + min(dp[i][j+1], dp[i+1][j+1], dp[i+1][j])
                    
                    
        return sum([sum(row) for row in dp])
# @lc code=end

