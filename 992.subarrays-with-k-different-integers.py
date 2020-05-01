#
# @lc app=leetcode id=992 lang=python3
#
# [992] Subarrays with K Different Integers
#
# https://leetcode.com/problems/subarrays-with-k-different-integers/description/
#
# algorithms
# Hard (46.73%)
# Likes:    787
# Dislikes: 15
# Total Accepted:    22.2K
# Total Submissions: 47.5K
# Testcase Example:  '[1,2,1,2,3]\n2'
#
# Given an array A of positive integers, call a (contiguous, not necessarily
# distinct) subarray of A good if the number of different integers in that
# subarray is exactly K.
# 
# (For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)
# 
# Return the number of good subarrays of A.
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [1,2,1,2,3], K = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers: [1,2],
# [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
# 
# 
# Example 2:
# 
# 
# Input: A = [1,2,1,3,4], K = 3
# Output: 3
# Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3],
# [2,1,3], [1,3,4].
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 20000
# 1 <= A[i] <= A.length
# 1 <= K <= A.length
# 
#

# @lc code=start
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        if K == 1:
            res, l, r = 0, 0, 0
            while l < len(A):
                count = 0
                while r < len(A) and A[l] == A[r]:
                    count += 1
                    r += 1
                res += (count*(count+1))//2
                l = r
            return res
        
        l, r, res, counts = 0, 0, 0, {}
        while l < len(A):
            leftRepeat, rightRepeat = 0,1
            while r < len(A) and len(counts) < K:
                if A[r] in counts:
                    counts[A[r]] += 1
                else:
                    counts[A[r]] = 1
                r += 1
            if len(counts) < K: break
            
            leftSearch, rightSearch = l, r
            while rightSearch < len(A) and A[rightSearch] in counts:
                rightRepeat += 1
                rightSearch += 1
            while len(counts) == K and leftSearch < r-1:
                counts[A[leftSearch]] -= 1
                if not counts[A[leftSearch]]:
                    del counts[A[leftSearch]]
                leftRepeat += 1
                leftSearch += 1
            res += leftRepeat * rightRepeat
            l = leftSearch
        return res
            

            
            



# @lc code=end

