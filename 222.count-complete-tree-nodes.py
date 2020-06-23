#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#
# https://leetcode.com/problems/count-complete-tree-nodes/description/
#
# algorithms
# Medium (42.97%)
# Likes:    1958
# Dislikes: 196
# Total Accepted:    216.4K
# Total Submissions: 487.6K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# Given a complete binary tree, count the number of nodes.
# 
# Note: 
# 
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is
# completely filled, and all nodes in the last level are as far left as
# possible. It can have between 1 and 2^h nodes inclusive at the last level h.
# 
# Example:
# 
# 
# Input: 
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# ⁠/ \  /
# 4  5 6
# 
# Output: 6
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
    def countNodes(self, root: TreeNode) -> int:
        """
        Time Complexity: O(lg(n)^2)
        """

        if not root:
            return 0
        leftDepth = self.depth(root.left)
        rightDepth = self.depth(root.right)
        if leftDepth == rightDepth:
            return 2**leftDepth + self.countNodes(root.right)
        else:
            return 2**rightDepth + self.countNodes(root.left)
        
    def depth(self, root):
        if not root:
            return 0
        return 1+self.depth(root.left)
# @lc code=end

