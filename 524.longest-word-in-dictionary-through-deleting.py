#
# @lc app=leetcode id=524 lang=python3
#
# [524] Longest Word in Dictionary through Deleting
#
# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/
#
# algorithms
# Medium (47.88%)
# Likes:    488
# Dislikes: 217
# Total Accepted:    62K
# Total Submissions: 129.6K
# Testcase Example:  '"abpcplea"\n["ale","apple","monkey","plea"]'
#
# 
# Given a string and a string dictionary, find the longest string in the
# dictionary that can be formed by deleting some characters of the given
# string. If there are more than one possible results, return the longest word
# with the smallest lexicographical order. If there is no possible result,
# return the empty string.
# 
# Example 1:
# 
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
# 
# Output: 
# "apple"
# 
# 
# 
# 
# Example 2:
# 
# Input:
# s = "abpcplea", d = ["a","b","c"]
# 
# Output: 
# "a"
# 
# 
# 
# Note:
# 
# All the strings in the input will only contain lower-case letters.
# The size of the dictionary won't exceed 1,000.
# The length of all the strings in the input won't exceed 1,000.
# 
# 
#

# @lc code=start
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        """
        Optimal solution: https://techdevguide.withgoogle.com/paths/foundational/find-longest-word-in-dictionary-that-subsequence-of-given-string/#
        Idea: 
        1. use a dictionary to fasten search;
        2. key: current letter; value: list of (w, idx) pairs
        3. Iterate through s, and update the dictionary:
            once idx == len(w), we get a match, check if we need to update res.
        """
        dic = {chr(x):[] for x in range(ord('a'), ord('z')+1)}
        res = ''
        for w in d:
            dic[w[0]].append((w, 0))
        for l in s:
            temp = []
            while dic[l]:
                w, idx = dic[l].pop()
                idx += 1
                if idx == len(w):
                    if len(w) > len(res): res = w
                    elif len(w) == len(res) and w < res: res = w
                elif l == w[idx]:
                    temp.append((w, idx))
                else:
                    dic[w[idx]].append((w, idx))
            dic[l] = temp
        return res
    # def findLongestWord(self, s: str, d: List[str]) -> str:
    #     """
    #     Sort first then search.
    #     """
    #     d = sorted(d, key = lambda x: (-len(x), x))
        
    #     def checkMatch(pattern, s):
    #         i, j = 0, 0
    #         while i < len(pattern):
    #             if j >= len(s): return False
    #             if pattern[i] == s[j]:
    #                 i += 1
    #             j += 1
    #         return True
    
    #     for pattern in d:
    #         if checkMatch(pattern, s): return pattern
    #     return ''

    # def findLongestWord(self, s: str, d: List[str]) -> str:
    #     """
    #     Without sorting.
    #     """
    #     def checkMatch(pattern, s):
    #         i, j = 0, 0
    #         while i < len(pattern):
    #             if j >= len(s): return False
    #             if pattern[i] == s[j]:
    #                 i += 1
    #             j += 1
    #         return True
    #     res = ''
    #     for pattern in d:
    #         if checkMatch(pattern, s):
    #             if len(pattern) > len(res): 
    #                 res = pattern
    #             elif len(pattern) ==  len(res) and pattern < res:
    #                 res = pattern
    #     return res
        
# @lc code=end

