#
# @lc app=leetcode id=1522 lang=python3
#
# [1522] Diameter of N-Ary Tree
#
# https://leetcode.com/problems/diameter-of-n-ary-tree/description/
#
# algorithms
# Medium (68.75%)
# Likes:    49
# Dislikes: 0
# Total Accepted:    1.9K
# Total Submissions: 2.7K
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# Given a root of an N-ary tree, you need to compute the length of the diameter
# of the tree.
# 
# The diameter of an N-ary tree is the length of the longest path between any
# two nodes in the tree. This path may or may not pass through the root.
# 
# (Nary-Tree input serialization is represented in their level order traversal,
# each group of children is separated by the null value.)
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [1,null,3,2,4,null,5,6]
# Output: 3
# Explanation: Diameter is shown in red color.
# 
# Example 2:
# 
# 
# 
# 
# Input: root = [1,null,2,null,3,4,null,5,null,6]
# Output: 4
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: root =
# [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: 7
# 
# 
# 
# Constraints:
# 
# 
# The depth of the n-ary tree is less than or equal to 1000.
# The total number of nodes is between [0, 10^4].
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        self.diameter = 0
        
        def helper(root):
            """
            Return the depth of the tree starting at root.
            Also update the self.diameter by searching through all subtrees
            """
            if not root or not root.children: return 0
            
            if len(root.children) == 1:
                depth = 1 + helper(root.children[0])
                self.diameter = max(self.diameter, depth)
                return depth
            
            else:
                depths = [1+helper(child) for child in root.children]
                max1, max2 = 0, 0
                for depth in depths:
                    if depth >= max1:
                        max1, max2 = depth, max1
                    elif depth < max1 and depth > max2:
                        max2 = depth
                self.diameter = max(self.diameter, max1+max2)
                return max1
        
        helper(root)
        
        return self.diameter
# @lc code=end

