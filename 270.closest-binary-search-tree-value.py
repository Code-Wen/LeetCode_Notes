"""
270. Closest Binary Search Tree Value

Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
"""
# Example:

# Input: root = [4,2,5,1,3], target = 3.714286

#     4
#    / \
#   2   5
#  / \
# 1   3

# Output: 4

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        res, diff = float('inf'), float('inf')
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            value = node.val
            cur_diff = abs(value - target)
            if cur_diff < diff:
                res, diff = value, cur_diff
            if value < target:
                if node.right:
                    queue.append(node.right)
            else:
                if node.left:
                    queue.append(node.left)
        return res

