#
# @lc app=leetcode id=1361 lang=python3
#
# [1361] Validate Binary Tree Nodes
#
# https://leetcode.com/problems/validate-binary-tree-nodes/description/
#
# algorithms
# Medium (56.86%)
# Likes:    128
# Dislikes: 35
# Total Accepted:    9K
# Total Submissions: 15.9K
# Testcase Example:  '4\n[1,-1,3,-1]\n[2,-1,-1,-1]'
#
# You have n binary tree nodes numbered from 0 to n - 1 where node i has two
# children leftChild[i] and rightChild[i], return true if and only if all the
# given nodes form exactly one valid binary tree.
# 
# If node i has no left child then leftChild[i] will equal -1, similarly for
# the right child.
# 
# Note that the nodes have no values and that we only use the node numbers in
# this problem.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
# Output: true
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
# Output: false
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
# Output: false
# 
# 
# Example 4:
# 
# 
# 
# 
# Input: n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^4
# leftChild.length == rightChild.length == n
# -1 <= leftChild[i], rightChild[i] <= n - 1
# 
# 
#

# @lc code=start
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
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

