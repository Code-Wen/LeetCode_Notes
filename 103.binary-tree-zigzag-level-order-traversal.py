#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (46.84%)
# Likes:    2147
# Dislikes: 101
# Total Accepted:    371.5K
# Total Submissions: 781.4K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the zigzag level order traversal of its nodes'
# values. (ie, from left to right, then right to left for the next level and
# alternate between).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its zigzag level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [20,9],
# ⁠ [15,7]
# ]
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        q, res, leftFirst, curLevel = collections.deque(), [], 1, []
        q.append(root)
        curCnt, nxtCnt = 1, 0
        while q:
            node = q.popleft()
            curLevel.append(node.val)
            curCnt -= 1
            if node.left:
                q.append(node.left)
                nxtCnt += 1
            if node.right:
                q.append(node.right)
                nxtCnt += 1
            if curCnt == 0:
                res = res+[curLevel] if leftFirst else res+[curLevel[::-1]]
                curLevel, curCnt, nxtCnt, leftFirst = [], nxtCnt, 0, (leftFirst+1)%2
        return res
# @lc code=end

