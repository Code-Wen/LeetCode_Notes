#
# @lc app=leetcode id=1443 lang=python3
#
# [1443] Minimum Time to Collect All Apples in a Tree
#
# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/description/
#
# algorithms
# Medium (58.21%)
# Likes:    223
# Dislikes: 16
# Total Accepted:    9K
# Total Submissions: 15.4K
# Testcase Example:  '7\n' +
  '[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]\n' +
  '[false,false,true,false,true,true,false]'
#
# Given an undirected tree consisting of n vertices numbered from 0 to n-1,
# which has some apples in their vertices. You spend 1 second to walk over one
# edge of the tree. Return the minimum time in seconds you have to spend in
# order to collect all apples in the tree starting at vertex 0 and coming back
# to this vertex.
# 
# The edges of the undirected tree are given in the array edges, where edges[i]
# = [fromi, toi] means that exists an edge connecting the vertices fromi and
# toi. Additionally, there is a boolean array hasApple, where hasApple[i] =
# true means that vertex i has an apple, otherwise, it does not have any
# apple.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple =
# [false,false,true,false,true,true,false]
# Output: 8 
# Explanation: The figure above represents the given tree where red vertices
# have an apple. One optimal path to collect all apples is shown by the green
# arrows.  
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple =
# [false,false,true,false,false,true,false]
# Output: 6
# Explanation: The figure above represents the given tree where red vertices
# have an apple. One optimal path to collect all apples is shown by the green
# arrows.  
# 
# 
# Example 3:
# 
# 
# Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple =
# [false,false,false,false,false,false,false]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^5
# edges.length == n-1
# edges[i].length == 2
# 0 <= fromi, toi <= n-1
# fromi < toi
# hasApple.length == n
# 
# 
#

# @lc code=start
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        n, res = len(hasApple), 0
        # record neighbors
        neighbors = [set() for i in range(n)]
        for i, j in edges:
          neighbors[i].add(j)
          neighbors[j].add(i)
        # compute distance between 0 and every point using BFS
        dist, seen, prevLayer, curDist = [0]*n,  {0}, {0}, 1
        while len(seen) < n:
          curLayer = set()
          for i in prevLayer:
            curLayer |= neighbors[i]
          curLayer -= seen
          for i in curLayer:
            dist[i] = curDist
          seen |= curLayer
          prevLayer = curLayer
          curDist += 1
        # build max heap wrt to the distance
        h = [(-dist[i],i) for i in range(n) if hasApple[i] and i!=0]
        apples = {x[1] for x in h}.union({0})
        heapq.heapify(h)
        # from apples further from 0
        # let them "crawl", one step at a time, to 0, merging along the way
        while h:
          d, i = heapq.heappop(h)
          res += 2
          apples.remove(i)
          for j in neighbors[i]:
            if dist[j] == - d - 1:
              if j not in apples:
                apples.add(j)
                heapq.heappush(h, (d+1,j))
              break
        return res



# @lc code=end

