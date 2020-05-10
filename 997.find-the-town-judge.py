#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#
# https://leetcode.com/problems/find-the-town-judge/description/
#
# algorithms
# Easy (50.11%)
# Likes:    620
# Dislikes: 66
# Total Accepted:    79.1K
# Total Submissions: 157K
# Testcase Example:  '2\n[[1,2]]'
#
# In a town, there are N people labelled from 1 to N.  There is a rumor that
# one of these people is secretly the town judge.
# 
# If the town judge exists, then:
# 
# 
# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# 
# 
# You are given trust, an array of pairs trust[i] = [a, b] representing that
# the person labelled a trusts the person labelled b.
# 
# If the town judge exists and can be identified, return the label of the town
# judge.  Otherwise, return -1.
# 
# 
# 
# Example 1:
# 
# 
# Input: N = 2, trust = [[1,2]]
# Output: 2
# 
# 
# 
# Example 2:
# 
# 
# Input: N = 3, trust = [[1,3],[2,3]]
# Output: 3
# 
# 
# 
# Example 3:
# 
# 
# Input: N = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1
# 
# 
# 
# Example 4:
# 
# 
# Input: N = 3, trust = [[1,2],[2,3]]
# Output: -1
# 
# 
# 
# Example 5:
# 
# 
# Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# Output: 3
# 
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 1000
# trust.length <= 10000
# trust[i] are all different
# trust[i][0] != trust[i][1]
# 1 <= trust[i][0], trust[i][1] <= N
# 
# 
#

# @lc code=start
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trusted = collections.defaultdict(list)
        candidates = {i for i in range(1,N+1)}
        for p, trustee in trust:
            candidates -= {p}
            if trustee in candidates:
                trusted[trustee].append(p)
        for cand in candidates:
            if len(trusted[cand]) == N-1: return cand
        return -1
# @lc code=end

