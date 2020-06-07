#
# @lc app=leetcode id=1457 lang=python3
#
# [1457] Pseudo-Palindromic Paths in a Binary Tree
#
# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/description/
#
# algorithms
# Medium (66.26%)
# Likes:    126
# Dislikes: 8
# Total Accepted:    11.2K
# Total Submissions: 16.9K
# Testcase Example:  '[2,3,1,3,1,null,1]'
#
# Given a binary tree where node values are digits from 1 to 9. A path in the
# binary tree is said to be pseudo-palindromic if at least one permutation of
# the node values in the path is a palindrome.
# 
# Return the number of pseudo-palindromic paths going from the root node to
# leaf nodes.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [2,3,1,3,1,null,1]
# Output: 2 
# Explanation: The figure above represents the given binary tree. There are
# three paths going from the root node to leaf nodes: the red path [2,3,3], the
# green path [2,1,1], and the path [2,3,1]. Among these paths only red path and
# green path are pseudo-palindromic paths since the red path [2,3,3] can be
# rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be
# rearranged in [1,2,1] (palindrome).
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: root = [2,1,1,1,3,null,null,null,null,null,1]
# Output: 1 
# Explanation: The figure above represents the given binary tree. There are
# three paths going from the root node to leaf nodes: the green path [2,1,1],
# the path [2,1,3,1], and the path [2,1]. Among these paths only the green path
# is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1]
# (palindrome).
# 
# 
# Example 3:
# 
# 
# Input: root = [9]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# The given binary tree will have between 1 and 10^5 nodes.
# Node values are digits from 1 to 9.
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
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        counts = [0]*10
        counts[root.val] = 1
        res, stack = 0, [(root, counts)]
        
        while stack:
            node, counts = stack.pop()
            if not node.left and not node.right:
                if sum([n%2==1 for n in counts]) < 2: res += 1
            else:
                if node.left:
                    temp = counts.copy()
                    temp[node.left.val] += 1
                    stack.append((node.left, temp))
                if node.right:
                    temp = counts.copy()
                    temp[node.right.val] += 1
                    stack.append((node.right, temp))
        return res

# @lc code=end

