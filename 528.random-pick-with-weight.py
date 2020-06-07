#
# @lc app=leetcode id=528 lang=python3
#
# [528] Random Pick with Weight
#
# https://leetcode.com/problems/random-pick-with-weight/description/
#
# algorithms
# Medium (43.79%)
# Likes:    661
# Dislikes: 1836
# Total Accepted:    84K
# Total Submissions: 192.6K
# Testcase Example:  '["Solution", "pickIndex"]\n[[[1]], []]'
#
# Given an array w of positive integers, where w[i] describes the weight of
# index i, write a function pickIndex which randomly picks an index in
# proportion to its weight.
# 
# Note:
# 
# 
# 1 <= w.length <= 10000
# 1 <= w[i] <= 10^5
# pickIndex will be called at most 10000 times.
# 
# 
# Example 1:
# 
# 
# Input: 
# ["Solution","pickIndex"]
# [[[1]],[]]
# Output: [null,0]
# 
# 
# 
# Example 2:
# 
# 
# Input: 
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output: [null,0,1,1,1,0]
# 
# 
# Explanation of Input Syntax:
# 
# The input is two lists: the subroutines called and their arguments.
# Solution's constructor has one argument, the array w. pickIndex has no
# arguments. Arguments are always wrapped with a list, even if there aren't
# any.
# 
#

# @lc code=start
class Solution:

    def __init__(self, w: List[int]):
        self.preSum = [0]*(len(w)+1)
        for i in range(1,len(w)+1):
            self.preSum[i] = w[i-1]+self.preSum[i-1]
        self.total = self.preSum[-1]

    def pickIndex(self) -> int:
        rand = random.randint(1, self.total)
        return self.binarySearch(rand)-1

    def binarySearch(self, n):
        #Find the index i such that self.preSum[i-1] < n <=self.preSum[i].
        l, r = 0, len(self.preSum)-1
        while l < r:
            mid = (l+r)//2
            if self.preSum[mid] >= n:
                r = mid
            else:
                l = mid+1
        return r


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end

