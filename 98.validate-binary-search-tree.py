#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (27.30%)
# Likes:    3356
# Dislikes: 475
# Total Accepted:    625.4K
# Total Submissions: 2.3M
# Testcase Example:  '[2,1,3]'
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
# 
# Assume a BST is defined as follows:
# 
# 
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# 
# 
# Example 1:
# 
# 
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 
# Input: [2,1,3]
# Output: true
# 
# 
# Example 2:
# 
# 
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
# 
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        d = list(range(n))
        degrees = [0]*n
        def find(x):
            if x != d[x]:
                d[x] = find(d[x])
            return d[x]
    
        def union(a,b):
            ra, rb = find(a), find(b)
            if d[ra] < d[rb]:
                d[rb] = ra
            else:
                d[ra] = rb
                
        for i in range(n):
            l, r = leftChild[i], rightChild[i]
            if l > -1:
                union(l, i)
                degrees[l] += 1
            if r > -1:
                union(r, i)
                degrees[r] += 1
        return sum(degrees) == n-1 and len({find(x) for x in range(n)}) == 1


        
# @lc code=end

