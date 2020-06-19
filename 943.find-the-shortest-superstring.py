#
# @lc app=leetcode id=943 lang=python3
#
# [943] Find the Shortest Superstring
#
# https://leetcode.com/problems/find-the-shortest-superstring/description/
#
# algorithms
# Hard (42.53%)
# Likes:    316
# Dislikes: 66
# Total Accepted:    10K
# Total Submissions: 23.4K
# Testcase Example:  '["alex","loves","leetcode"]'
#
# Given an array A of strings, find any smallest string that contains each
# string in A as a substring.
# 
# We may assume that no string in A is substring of another string in A.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: ["alex","loves","leetcode"]
# Output: "alexlovesleetcode"
# Explanation: All permutations of "alex","loves","leetcode" would also be
# accepted.
# 
# 
# 
# Example 2:
# 
# 
# Input: ["catg","ctaagt","gcta","ttca","atgcatc"]
# Output: "gctaagttcatgcatc"
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 12
# 1 <= A[i].length <= 20
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:
        #https://leetcode.com/problems/find-the-shortest-superstring/discuss/195487/python-bfs-solution-with-detailed-explanation(with-extra-Chinese-explanation)
        def getDistance(s1, s2):
            for i in range(1, len(s1)):
                if s2.startswith(s1[i:]):
                    return len(s1) - i
            return 0

        def pathtoStr(A, G, path):
            res = A[path[0]]
            for i in range(1, len(path)):
                res += A[path[i]][G[path[i-1]][path[i]]:]
            return res

        n = len(A)
        G = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                G[i][j] = getDistance(A[i], A[j])
                G[j][i] = getDistance(A[j], A[i])

        d = [[0]*n for _ in range(1<<n)]
        Q = collections.deque([(i, 1<<i, [i], 0) for i in range(n)])
        l = -1 # record the maximum s_len
        P = [] # record the path corresponding to maximum s_len
        while Q:
            node, mask, path, dis = Q.popleft()
            if dis < d[mask][node]: continue
            if mask == (1<<n) - 1 and dis > l:
                P,l = path,dis
                continue
            for i in range(n):
                nex_mask = mask | (1<<i)
                # case1: make sure that each node is only traversed once
                # case2: only if we can get larger save length, we consider it.
                if nex_mask != mask and d[mask][node] + G[node][i] >= d[nex_mask][i]:
                    d[nex_mask][i] = d[mask][node] + G[node][i]
                    Q.append((i, nex_mask, path+[i], d[nex_mask][i]))

        return pathtoStr(A,G,P)
# @lc code=end

