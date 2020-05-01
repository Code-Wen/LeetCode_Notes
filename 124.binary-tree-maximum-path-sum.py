#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (32.74%)
# Likes:    3024
# Dislikes: 247
# Total Accepted:    312.6K
# Total Submissions: 946.5K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty binary tree, find the maximum path sum.
# 
# For this problem, a path is defined as any sequence of nodes from some
# starting node to any node in the tree along the parent-child connections. The
# path must contain at least one node and does not need to go through the
# root.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# 
# ⁠      1
# ⁠     / \
# ⁠    2   3
# 
# Output: 6
# 
# 
# Example 2:
# 
# 
# Input: [-10,9,20,null,null,15,7]
# 
# -10
# / \
# 9  20
# /  \
# 15   7
# 
# Output: 42
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
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float('-inf')
        def helper(node):
            if not node: return
            leftSum = 0 if not node.left else helper(node.left)
            rightSum = 0 if not node.right else helper(node.right)
            choice = max([0, leftSum, rightSum])
            res = node.val + choice
            self.res = max(self.res, node.val + max(choice, leftSum+rightSum))
            return res
        
        helper(root)
        return self.res
# @lc code=end

