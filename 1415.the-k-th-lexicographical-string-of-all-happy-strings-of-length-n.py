#
# @lc app=leetcode id=1415 lang=python3
#
# [1415] The k-th Lexicographical String of All Happy Strings of Length n
#
# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/
#
# algorithms
# Medium (68.21%)
# Likes:    46
# Dislikes: 1
# Total Accepted:    3.4K
# Total Submissions: 4.9K
# Testcase Example:  '1\n3'
#
# A happy string is a string that:
# 
# 
# consists only of letters of the set ['a', 'b', 'c'].
# s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is
# 1-indexed).
# 
# 
# For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings
# and strings "aa", "baa" and "ababbc" are not happy strings.
# 
# Given two integers n and k, consider a list of all happy strings of length n
# sorted in lexicographical order.
# 
# Return the kth string of this list or return an empty string if there are
# less than k happy strings of length n.
# 
# 
# Example 1:
# 
# 
# Input: n = 1, k = 3
# Output: "c"
# Explanation: The list ["a", "b", "c"] contains all happy strings of length 1.
# The third string is "c".
# 
# 
# Example 2:
# 
# 
# Input: n = 1, k = 4
# Output: ""
# Explanation: There are only 3 happy strings of length 1.
# 
# 
# Example 3:
# 
# 
# Input: n = 3, k = 9
# Output: "cab"
# Explanation: There are 12 different happy string of length 3 ["aba", "abc",
# "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You
# will find the 9th string = "cab"
# 
# 
# Example 4:
# 
# 
# Input: n = 2, k = 7
# Output: ""
# 
# 
# Example 5:
# 
# 
# Input: n = 10, k = 100
# Output: "abacbabacb"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10
# 1 <= k <= 100
# 
# 
# 
#

# @lc code=start
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # Check whether we can generate enough strings or not
        if 3*(2**(n-1)) < k: return ''
        
        def choose(to_exclude, large):
            """
            to_exclude: the letter to exclude
            large: whether we choose the larger or smaller letter
            
            return: the letter of choice
            """
            choices = {'a','b','c'} - {to_exclude}
            if large:
                return max(choices)
            else:
                return min(choices)
        
        # Choose the first letter
        mod = 2**(n-1)
        res, k, mod = 'abc'[(k-1)//mod], (k-1)%mod, mod//2
        
        # Chooese the rest letters one by one
        while len(res) < n:
            to_exclude = res[-1]
            res += choose(to_exclude, k//mod)
            k, mod = k%mod, mod//2
        return res
# @lc code=end

