#
# @lc app=leetcode id=623 lang=python3
#
# [623] Add One Row to Tree
#
# https://leetcode.com/problems/add-one-row-to-tree/description/
#
# algorithms
# Medium (49.74%)
# Likes:    445
# Dislikes: 133
# Total Accepted:    38.7K
# Total Submissions: 77.8K
# Testcase Example:  '[4,2,6,3,1,5]\n1\n2'
#
# Given the root of a binary tree, then value v and depth d, you need to add a
# row of nodes with value v at the given depth d. The root node is at depth
# 1. 
# 
# The adding rule is: given a positive integer depth d, for each NOT null tree
# nodes N in depth d-1, create two tree nodes with value v as N's left subtree
# root and right subtree root. And N's original left subtree should be the left
# subtree of the new left subtree root, its original right subtree should be
# the right subtree of the new right subtree root. If depth d is 1 that means
# there is no depth d-1 at all, then create a tree node with value v as the new
# root of the whole original tree, and the original tree is the new root's left
# subtree.
# 
# Example 1:
# 
# Input: 
# A binary tree as following:
# ⁠      4
# ⁠    /   \
# ⁠   2     6
# ⁠  / \   / 
# ⁠ 3   1 5   
# 
# v = 1
# 
# d = 2
# 
# Output: 
# ⁠      4
# ⁠     / \
# ⁠    1   1
# ⁠   /     \
# ⁠  2       6
# ⁠ / \     / 
# ⁠3   1   5   
# 
# 
# 
# 
# 
# Example 2:
# 
# Input: 
# A binary tree as following:
# ⁠     4
# ⁠    /   
# ⁠   2    
# ⁠  / \   
# ⁠ 3   1    
# 
# v = 1
# 
# d = 3
# 
# Output: 
# ⁠     4
# ⁠    /   
# ⁠   2
# ⁠  / \    
# ⁠ 1   1
# ⁠/     \  
# 3       1
# 
# 
# 
# Note:
# 
# The given d is in range [1, maximum depth of the given tree + 1].
# The given binary tree has at least one tree node.
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
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1: 
            return TreeNode(v, root, None)
        que, goal = collections.deque([(root, 1)]), d-1
        while que:
            node, depth = que.popleft()
            if depth == goal:
                node.left = TreeNode(v, node.left, None)
                node.right = TreeNode(v, None, node.right)
            else:
                if node.left:
                    que.append((node.left, depth+1))
                if node.right:
                    que.append((node.right, depth+1))
        return root
        
# @lc code=end

