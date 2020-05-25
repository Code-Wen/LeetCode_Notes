#
# @lc app=leetcode id=1442 lang=python3
#
# [1442] Count Triplets That Can Form Two Arrays of Equal XOR
#
# https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/description/
#
# algorithms
# Medium (67.24%)
# Likes:    178
# Dislikes: 13
# Total Accepted:    8.6K
# Total Submissions: 12.8K
# Testcase Example:  '[2,3,1,6,7]'
#
# Given an array of integers arr.
# 
# We want to select three indices i, j and k where (0 <= i < j <= k <
# arr.length).
# 
# Let's define a and b as follows:
# 
# 
# a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
# b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
# 
# 
# Note that ^ denotes the bitwise-xor operation.
# 
# Return the number of triplets (i, j and k) Where a == b.
# 
# 
# Example 1:
# 
# 
# Input: arr = [2,3,1,6,7]
# Output: 4
# Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
# 
# 
# Example 2:
# 
# 
# Input: arr = [1,1,1,1,1]
# Output: 10
# 
# 
# Example 3:
# 
# 
# Input: arr = [2,3]
# Output: 0
# 
# 
# Example 4:
# 
# 
# Input: arr = [1,3,5,7,9]
# Output: 3
# 
# 
# Example 5:
# 
# 
# Input: arr = [7,11,12,9,5,2,7,17,22]
# Output: 8
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 300
# 1 <= arr[i] <= 10^8
# 
#

# @lc code=start
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # Since arr[i]!= 0, every triple (i,j,k)
        # satisfying the conditions must also satisfy
        # arr[i]^ ...arr[k] == 0;
        # Once we find i and k such that arr[i]^ ...arr[k] == 0,
        # then for every i<j<=k, we have a triple (i,j,k).
        # Thus a total of k-i triples.
        prefix, suffix = copy.copy(arr), copy.copy(arr)
        for i in range(1, len(arr)):
            prefix[i] ^= prefix[i-1]
            suffix[-i-1] ^= suffix[-i]
        res = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                n1 = prefix[i-1] if i else 0
                n2 = suffix[j+1] if j+1<len(arr) else 0
                blockRes = n1^n2^prefix[-1]
                if blockRes == 0: res += j-i
        return res

        
# @lc code=end

