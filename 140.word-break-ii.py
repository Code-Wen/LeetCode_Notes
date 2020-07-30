#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#
# https://leetcode.com/problems/word-break-ii/description/
#
# algorithms
# Hard (31.28%)
# Likes:    2088
# Dislikes: 387
# Total Accepted:    244.2K
# Total Submissions: 765.1K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, add spaces in s to construct a sentence where each word is a
# valid dictionary word. Return all such possible sentences.
# 
# Note:
# 
# 
# The same word in the dictionary may be reused multiple times in the
# segmentation.
# You may assume the dictionary does not contain duplicate words.
# 
# 
# Example 1:
# 
# 
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
# "cats and dog",
# "cat sand dog"
# ]
# 
# 
# Example 2:
# 
# 
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
# "pine apple pen apple",
# "pineapple pen apple",
# "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []
# 
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        
        memo = collections.defaultdict(list)
        
        def _wordBreak_topdown(s):
            if not s:
                return [[]]
            if s in memo:
                return memo[s]
            
            for endIndex in range(1, len(s)+1):
                word = s[:endIndex]
                if word in wordSet:
                    for subsentence in _wordBreak_topdown(s[endIndex:]):
                        memo[s].append([word]+subsentence)
            return memo[s]
        
        _wordBreak_topdown(s)
        
        return [" ".join(words) for words in memo[s]]
# @lc code=end

