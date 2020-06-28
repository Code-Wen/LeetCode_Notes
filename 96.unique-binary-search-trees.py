#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#
# https://leetcode.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (50.94%)
# Likes:    3252
# Dislikes: 118
# Total Accepted:    292K
# Total Submissions: 562.4K
# Testcase Example:  '3'
#
# Given n, how many structurally unique BST's (binary search trees) that store
# values 1 ... n?
# 
# Example:
# 
# 
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
# 
# 
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        if n in {0,1}: return 1
        
        d ={1:1, 0:1}
        for k in range(2,n+1):
            res = 0
            for i in range(1, k+1):
                res += d[i-1]*d[k-i]
            d[k] = res
        
        return d[n]
# @lc code=end

