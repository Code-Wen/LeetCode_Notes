#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#
# https://leetcode.com/problems/sum-of-left-leaves/description/
#
# algorithms
# Easy (50.96%)
# Likes:    1348
# Dislikes: 137
# Total Accepted:    200.9K
# Total Submissions: 388.6K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Find the sum of all left leaves in a given binary tree.
# 
# Example:
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# There are two left leaves in the binary tree, with values 9 and 15
# respectively. Return 24.
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        res = 0
        stack = [(root,0)] if root else []
        while stack:
            node, left = stack.pop()
            if not node.left and not node.right and left:
                res += node.val
                continue
            if node.left:
                stack.append((node.left, 1))
            if node.right:
                stack.append((node.right, 0))
        return res
# @lc code=end

