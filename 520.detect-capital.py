#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#
# https://leetcode.com/problems/detect-capital/description/
#
# algorithms
# Easy (53.29%)
# Likes:    573
# Dislikes: 273
# Total Accepted:    141.3K
# Total Submissions: 259.3K
# Testcase Example:  '"USA"'
#
# Given a word, you need to judge whether the usage of capitals in it is right
# or not.
# 
# We define the usage of capitals in a word to be right when one of the
# following cases holds:
# 
# 
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# 
# Otherwise, we define that this word doesn't use capitals in a right way.
# 
# 
# 
# Example 1:
# 
# 
# Input: "USA"
# Output: True
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: "FlaG"
# Output: False
# 
# 
# 
# 
# Note: The input will be a non-empty word consisting of uppercase and
# lowercase latin letters.
# 
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if not word: return True
        firstUpper = word[0].isupper()
        allUpper, allLower = all([l.isupper() for l in word[1:]]), all([l.islower() for l in word[1:]])
        return  (allUpper or allLower) if firstUpper else allLower
# @lc code=end

