#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#
# https://leetcode-cn.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (39.28%)
# Likes:    525
# Dislikes: 0
# Total Accepted:    39.2K
# Total Submissions: 99.7K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
# 
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
# 
# 
# 
# 
# 
# 以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。
# 
# 
# 
# 
# 
# 图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。
# 
# 
# 
# 示例:
# 
# 输入: [2,1,5,6,2,3]
# 输出: 10
# 
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        For any bar x, if it's in a rectangle of which the height is also the height of x, we know that every bar in the rectangle must be no shorter than x. Then the issue is to find the left and right boundary where the bars are shorter than x. According to the code, when a bar is popped out from the stack, we know it must be higher than the bar at position i, so bar[i] must be the right boundary (exclusive) of the rectangle, and the previous bar in the stack is the first one that is shorter than the popped one so it must be the left boundary (also exclusive). Then we find the rectangle.
        """
        heights += [0]
        stack, ans = [-1], 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - 1 - stack[-1]
                ans = max(ans, h * w)
            stack.append(i)
        return ans


# @lc code=end

