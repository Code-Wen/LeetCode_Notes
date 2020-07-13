#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#
# https://leetcode.com/problems/same-tree/description/
#
# algorithms
# Easy (52.57%)
# Likes:    2137
# Dislikes: 60
# Total Accepted:    560K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# Given two binary trees, write a function to check if they are the same or
# not.
# 
# Two binary trees are considered the same if they are structurally identical
# and the nodes have the same value.
# 
# Example 1:
# 
# 
# Input:     1         1
# ⁠         / \       / \
# ⁠        2   3     2   3
# 
# ⁠       [1,2,3],   [1,2,3]
# 
# Output: true
# 
# 
# Example 2:
# 
# 
# Input:     1         1
# ⁠         /           \
# ⁠        2             2
# 
# ⁠       [1,2],     [1,null,2]
# 
# Output: false
# 
# 
# Example 3:
# 
# 
# Input:     1         1
# ⁠         / \       / \
# ⁠        2   1     1   2
# 
# ⁠       [1,2,1],   [1,1,2]
# 
# Output: false
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
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        Another approach is to traverse both trees inplace, then compare the two lists.
        """
        if (q and not p) or (p and not q): return False
        if not p and not q: return True
        
        q1,q2 = collections.deque([p]), collections.deque([q])
        while q1:
            node1, node2 = q1.popleft(), q2.popleft()
            if node1.val != node2.val: return False
            if (node1.left and not node2.left) or (node2.left and not node1.left):
                return False
            if node1.left:
                q1.append(node1.left)
                q2.append(node2.left)
            if (node1.right and not node2.right) or (node2.right and not node1.right):
                return False
            if node1.right:
                q1.append(node1.right)
                q2.append(node2.right)
        return True
# @lc code=end

