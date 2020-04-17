#
# @lc app=leetcode id=1408 lang=python3
#
# [1408] String Matching in an Array
#
# https://leetcode.com/problems/string-matching-in-an-array/description/
#
# algorithms
# Easy (58.79%)
# Likes:    27
# Dislikes: 20
# Total Accepted:    9.6K
# Total Submissions: 16.4K
# Testcase Example:  '["mass","as","hero","superhero"]'
#
# Given an array of string words. Return all strings in words which is
# substring of another word in any order. 
# 
# String words[i] is substring of words[j], if can be obtained removing some
# characters to left and/or right side of words[j].
# 
# 
# Example 1:
# 
# 
# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is substring of "mass" and "hero" is substring of
# "superhero".
# ["hero","as"] is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: words = ["leetcode","et","code"]
# Output: ["et","code"]
# Explanation: "et", "code" are substring of "leetcode".
# 
# 
# Example 3:
# 
# 
# Input: words = ["blue","green","bu"]
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# 1 <= words.length <= 100
# 1 <= words[i].length <= 30
# words[i] contains only lowercase English letters.
# It's guaranteed that words[i] will be unique.
# 
#

# @lc code=start
class Solution:
    # def stringMatching(self, words: List[str]) -> List[str]:
    #     words = sorted(words, key = lambda x: len(x))
    #     res = []
    #     for i, word in enumerate(words):
    #         for w in words[i+1:]:
    #             if w.find(word) > -1:
    #                 res.append(word)
    #                 break
    #     return res

    def stringMatching(self, words: List[str]) -> List[str]:
        def add(word: str):
            node = trie
            for c in word:
                node = node.setdefault(c, {})

        def get(word: str) -> bool:
            node = trie
            for c in word:
                if (node := node.get(c)) is None: return False
            return True

        words.sort(key=len, reverse=True)
        trie, result = {}, []
        for word in words:
            if get(word): result.append(word)
            for i in range(len(word)):
                add(word[i:])
        return result
# @lc code=end

