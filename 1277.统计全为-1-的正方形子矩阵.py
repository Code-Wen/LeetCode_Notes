#
# @lc app=leetcode.cn id=1277 lang=python3
#
# [1277] 统计全为 1 的正方形子矩阵
#
# https://leetcode-cn.com/problems/count-square-submatrices-with-all-ones/description/
#
# algorithms
# Medium (66.63%)
# Likes:    36
# Dislikes: 0
# Total Accepted:    3.7K
# Total Submissions: 5.6K
# Testcase Example:  '[[0,1,1,1],[1,1,1,1],[0,1,1,1]]'
#
# 给你一个 m * n 的矩阵，矩阵中的元素不是 0 就是 1，请你统计并返回其中完全由 1 组成的 正方形 子矩阵的个数。
# 
# 
# 
# 示例 1：
# 
# 输入：matrix =
# [
# [0,1,1,1],
# [1,1,1,1],
# [0,1,1,1]
# ]
# 输出：15
# 解释： 
# 边长为 1 的正方形有 10 个。
# 边长为 2 的正方形有 4 个。
# 边长为 3 的正方形有 1 个。
# 正方形的总数 = 10 + 4 + 1 = 15.
# 
# 
# 示例 2：
# 
# 输入：matrix = 
# [
# ⁠ [1,0,1],
# ⁠ [1,1,0],
# ⁠ [1,1,0]
# ]
# 输出：7
# 解释：
# 边长为 1 的正方形有 6 个。 
# 边长为 2 的正方形有 1 个。
# 正方形的总数 = 6 + 1 = 7.
# 
# 
# 
# 
# 提示：
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

