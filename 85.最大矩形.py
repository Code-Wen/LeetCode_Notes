#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#
# https://leetcode-cn.com/problems/maximal-rectangle/description/
#
# algorithms
# Hard (45.24%)
# Likes:    374
# Dislikes: 0
# Total Accepted:    23.7K
# Total Submissions: 52.3K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
# 
# 示例:
# 
# 输入:
# [
# ⁠ ["1","0","1","0","0"],
# ⁠ ["1","0","1","1","1"],
# ⁠ ["1","1","1","1","1"],
# ⁠ ["1","0","0","1","0"]
# ]
# 输出: 6
# 
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # For each row, compute the height of the histogram based on that row.
        # Then compute the largest rectangle in the histogram by the method from Problem 84.
        if not matrix or not matrix[0]: return 0
        n, ans = len(matrix[0]), 0
        heights = [0]*(n+1)

        def findMaxRectangleInHistogram(h):
            stack, res = [-1], 0
            for i in range(len(h)):
                while h[i] < h[stack[-1]]:
                    height = h[stack.pop()]
                    w = i - 1 - stack[-1]
                    res = max(res, height * w)
                stack.append(i)
            return res

        for row in matrix:
            for i in range(n):
                heights[i] = heights[i]+1 if row[i]=='1' else 0
            ans = max(ans, findMaxRectangleInHistogram(heights))
        return ans
        

# @lc code=end

