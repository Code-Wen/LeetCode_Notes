#
# @lc app=leetcode id=1044 lang=python3
#
# [1044] Longest Duplicate Substring
#
# https://leetcode.com/problems/longest-duplicate-substring/description/
#
# algorithms
# Hard (25.80%)
# Likes:    348
# Dislikes: 168
# Total Accepted:    13.3K
# Total Submissions: 48.2K
# Testcase Example:  '"banana"'
#
# Given a string S, consider all duplicated substrings: (contiguous) substrings
# of S that occur 2 or more times.  (The occurrences may overlap.)
# 
# Return any duplicated substring that has the longest possible length.  (If S
# does not have a duplicated substring, the answer is "".)
# 
# 
# 
# Example 1:
# 
# 
# Input: "banana"
# Output: "ana"
# 
# 
# Example 2:
# 
# 
# Input: "abcd"
# Output: ""
# 
# 
# 
# 
# Note:
# 
# 
# 2 <= S.length <= 10^5
# S consists of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    
    def RabinKarp(self,text, L, mod):
        '''
        The Rabin-Karp algorithm to find matches with length L.
        The hashmap for text[i:i+L] is computed as 
        ord(text[i])*pow(base, L-1)+ ord(text[i+1])*pow(base, L-2) + ... + ord(text[i+L-1])*pow(base, 0)
        '''
        if L == 0: return True
        hashRes, base = 0, 256
        # Power for the first letter. Used to update hashRes
        power = (base**(L-1))%mod

        dic = collections.defaultdict(list)

        for i in range(L): 
            hashRes = (base * hashRes + ord(text[i]))% mod

        dic[hashRes].append(0)

        for i in range(len(text) - L):
            hashRes = (base*(hashRes-ord(text[i])*power) + ord(text[i + L]))% mod
            for j in dic[hashRes]:
                if text[i+1:i+L+1] == text[j:j+L]:
                    return (True, text[j:j+L])
            dic[hashRes].append(i+1)
        return (False, "")

    def longestDupSubstring(self, S):
        beg, end = 0, len(S)
        q = (1<<31) - 1 
        Found = ""
        while beg + 1 < end:
            mid = (beg + end)//2
            isFound, candidate = self.RabinKarp(S, mid, q)
            if isFound:
                beg, Found = mid, candidate
            else:
                end = mid

        return Found
# @lc code=end

