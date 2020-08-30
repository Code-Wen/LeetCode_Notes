#
# @lc app=leetcode id=952 lang=python3
#
# [952] Largest Component Size by Common Factor
#
# https://leetcode.com/problems/largest-component-size-by-common-factor/description/
#
# algorithms
# Hard (30.27%)
# Likes:    329
# Dislikes: 52
# Total Accepted:    14.7K
# Total Submissions: 44.6K
# Testcase Example:  '[4,6,15,35]'
#
# Given a non-empty array of unique positive integers A, consider the following
# graph:
# 
# 
# There are A.length nodes, labelled A[0] to A[A.length - 1];
# There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a
# common factor greater than 1.
# 
# 
# Return the size of the largest connected component in the graph.
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
# Input: [4,6,15,35]
# Output: 4
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: [20,50,9,63]
# Output: 2
# 
# 
# 
# 
# Example 3:
# 
# 
# Input: [2,3,6,7,4,12,21,39]
# Output: 8
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 20000
# 1 <= A[i] <= 100000
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def findPrimeFactors(num):
            factor = 2
            primeFactors = set()
            while num >= factor * factor:
                if num%factor == 0:
                    primeFactors.add(factor)
                    num = num//factor
                else:
                    factor += 1
            primeFactors.add(num)
            return primeFactors
        
        uf = unionFind(max(A))
        num_factor_map = {}
        
        for num in A:
            primeFactors = list(findPrimeFactors(num))
            
            num_factor_map[num] = primeFactors[0]
            
            for i in range(len(primeFactors)-1):
                uf.union(primeFactors[i], primeFactors[i+1])
        
        res = 0
        group_count = collections.defaultdict(int)
        for num in A:
            group_id = uf.find(num_factor_map[num])
            group_count[group_id] += 1
            res = max(res, group_count[group_id] )
        
        return res
                    
        

        
class unionFind:
    
    def __init__(self, size):
        self.parent = [i for i in range(size+1)]
        self.size = [1]*(size+1)
    
    def find(self,x):
        """
        Return the component id that element x belongs to
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """
        Merge the components that x, y belongs to respectively,
        return the merged component id.
        """
        px, py = self.find(x), self.find(y)
        
        if px == py:
            return px
        
        if self.size[px] > self.size[py]:
            px,py = py, px
        
        self.parent[px] = py
        self.size[py] += self.size[px]
        
        return py
# @lc code=end

