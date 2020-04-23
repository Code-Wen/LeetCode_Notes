#
# @lc app=leetcode id=1417 lang=python3
#
# [1417] Reformat The String
#
# https://leetcode.com/problems/reformat-the-string/description/
#
# algorithms
# Easy (55.59%)
# Likes:    26
# Dislikes: 18
# Total Accepted:    8K
# Total Submissions: 14.4K
# Testcase Example:  '"a0b1c2"'
#
# Given alphanumeric string s. (Alphanumeric string is a string consisting of
# lowercase English letters and digits).
# 
# You have to find a permutation of the string where no letter is followed by
# another letter and no digit is followed by another digit. That is, no two
# adjacent characters have the same type.
# 
# Return the reformatted string or return an empty string if it is impossible
# to reformat the string.
# 
# 
# Example 1:
# 
# 
# Input: s = "a0b1c2"
# Output: "0a1b2c"
# Explanation: No two adjacent characters have the same type in "0a1b2c".
# "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.
# 
# 
# Example 2:
# 
# 
# Input: s = "leetcode"
# Output: ""
# Explanation: "leetcode" has only characters so we cannot separate them by
# digits.
# 
# 
# Example 3:
# 
# 
# Input: s = "1229857369"
# Output: ""
# Explanation: "1229857369" has only digits so we cannot separate them by
# characters.
# 
# 
# Example 4:
# 
# 
# Input: s = "covid2019"
# Output: "c2o0v1i9d"
# 
# 
# Example 5:
# 
# 
# Input: s = "ab123"
# Output: "1a2b3"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 500
# s consists of only lowercase English letters and/or digits.
# 
# 
#

# @lc code=start
class Solution:
    def reformat(self, s: str) -> str:
        digits, letters = [], []
        for l in s:
            if l.isdigit():
                digits.append(l)
            else:
                letters.append(l)
        res = ''
        if abs(len(digits)-len(letters))>1:
            return res
        if len(digits) >= len(letters):
            more, less = digits, letters
        else:
            more, less = letters, digits
        
        while less:
            res += more.pop()
            res += less.pop()
        if more: res += more.pop()
        return res
        
# @lc code=end

