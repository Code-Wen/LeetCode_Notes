#
# @lc app=leetcode id=889 lang=python3
#
# [889] Construct Binary Tree from Preorder and Postorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/
#
# algorithms
# Medium (65.06%)
# Likes:    702
# Dislikes: 44
# Total Accepted:    32.7K
# Total Submissions: 50.2K
# Testcase Example:  '[1,2,4,5,3,6,7]\n[4,5,2,6,7,3,1]'
#
# Return any binary tree that matches the given preorder and postorder
# traversals.
# 
# Values in the traversals pre and post are distinct positive integers.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
# Output: [1,2,3,4,5,6,7]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= pre.length == post.length <= 30
# pre[] and post[] are both permutations of 1, 2, ..., pre.length.
# It is guaranteed an answer exists. If there exists multiple answers, you can
# return any of them.
# 
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
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        n =  len(pre)
        def helper(leftPre, rightPre, leftPost, rightPost):
            """
            return: the root node from the lists pre[leftPre:rightPre], post[leftPost: rightPost]
            """
            if leftPre >= rightPre: return None

            root = TreeNode(pre[leftPre])
            if leftPre + 1 < rightPre:
                # Value of the left child of root
                val = pre[leftPre+1]
                # Locate the index of the left child in post
                idx = post[leftPost:rightPost].index(val) + leftPost
                # Formulas for the end points come from the fact that the subarrays of pre and post have to be of the same length
                root.left = helper(leftPre+1, idx+2+leftPre-leftPost, leftPost,idx+1)
                root.right = helper(idx+2+rightPre-rightPost, rightPre, idx+1,rightPost-1)
            
            return root
        return helper(0,n,0,n)
# @lc code=end

