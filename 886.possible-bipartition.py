#
# @lc app=leetcode id=886 lang=python3
#
# [886] Possible Bipartition
#
# https://leetcode.com/problems/possible-bipartition/description/
#
# algorithms
# Medium (43.30%)
# Likes:    637
# Dislikes: 19
# Total Accepted:    32.7K
# Total Submissions: 76.8K
# Testcase Example:  '4\n[[1,2],[1,3],[2,4]]'
#
# Given a set of N people (numbered 1, 2, ..., N), we would like to split
# everyone into two groups of any size.
# 
# Each person may dislike some other people, and they should not go into the
# same group. 
# 
# Formally, if dislikes[i] = [a, b], it means it is not allowed to put the
# people numbered a and b into the same group.
# 
# Return true if and only if it is possible to split everyone into two groups
# in this way.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: group1 [1,4], group2 [2,3]
# 
# 
# 
# Example 2:
# 
# 
# Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false
# 
# 
# 
# Example 3:
# 
# 
# Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# Output: false
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 2000
# 0 <= dislikes.length <= 10000
# 1 <= dislikes[i][j] <= N
# dislikes[i][0] < dislikes[i][1]
# There does not exist i != j for which dislikes[i] == dislikes[j].
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        d, needArrange = collections.defaultdict(set), set()
        for i, j in dislikes:
            d[i].add(j)
            d[j].add(i)
            needArrange |= {i,j}
                            
        groups, stacks = [set(),set()], [[],[]]
        def checkStack(j, needArrange):
            while stacks[j]:
                    k = stacks[j].pop()
                    for i in d[k]:
                        if i in groups[j]: return False
                        elif i in groups[(j+1)%2]: continue
                        else:
                            groups[(j+1)%2].add(i)
                            stacks[(j+1)%2].append(i)
                            needArrange -= {i}
            return True
        while needArrange:
            if stacks[0] or stacks[1]:
                if not checkStack(0,needArrange): return False
                if not checkStack(1,needArrange): return False
            else: 
                start = needArrange.pop()
                if start in groups[0] or start in groups[1]: return False
                groups[0].add(start)
                stacks[0].append(start)
            
        if stacks[0] or stacks[1]:
            if not checkStack(0,needArrange): return False
            if not checkStack(1,needArrange): return False
        return True
        
# @lc code=end

