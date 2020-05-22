#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#
# https://leetcode.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (40.71%)
# Likes:    1353
# Dislikes: 54
# Total Accepted:    111.8K
# Total Submissions: 257.4K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# Given two strings s1 and s2, write a function to return true if s2 contains
# the permutation of s1. In other words, one of the first string's permutations
# is the substring of the second string.
# 
# 
# 
# Example 1:
# 
# 
# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").
# 
# 
# Example 2:
# 
# 
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
# 
# 
# 
# 
# Note:
# 
# 
# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].
# 
# 
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        d1, n1 = collections.Counter(s1), len(s1)
        d2 = collections.defaultdict(int)
        for l in s2[:n1]:
            d2[l] += 1
        def compare():
            for l in d1:
                if d2[l]!=d1[l]:
                    return False
            return True
        if compare(): return True
        for i in range(n1, len(s2)):
            d2[s2[i]] += 1
            d2[s2[i-n1]] -= 1
            if compare(): return True
        return False
# @lc code=end

