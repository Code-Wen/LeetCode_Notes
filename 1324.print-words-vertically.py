#
# @lc app=leetcode id=1324 lang=python3
#
# [1324] Print Words Vertically
#
# https://leetcode.com/problems/print-words-vertically/description/
#
# algorithms
# Medium (58.34%)
# Likes:    94
# Dislikes: 41
# Total Accepted:    10.4K
# Total Submissions: 17.8K
# Testcase Example:  '"HOW ARE YOU"'
#
# Given a string s. Return all the words vertically in the same order in which
# they appear in s.
# Words are returned as a list of strings, complete with spaces when is
# necessary. (Trailing spaces are not allowed).
# Each word would be put on only one column and that in one column there will
# be only one word.
# 
# 
# Example 1:
# 
# 
# Input: s = "HOW ARE YOU"
# Output: ["HAY","ORO","WEU"]
# Explanation: Each word is printed vertically. 
# ⁠"HAY"
# "ORO"
# "WEU"
# 
# 
# Example 2:
# 
# 
# Input: s = "TO BE OR NOT TO BE"
# Output: ["TBONTB","OEROOE","   T"]
# Explanation: Trailing spaces is not allowed. 
# "TBONTB"
# "OEROOE"
# "   T"
# 
# 
# Example 3:
# 
# 
# Input: s = "CONTEST IS COMING"
# Output: ["CIC","OSO","N M","T I","E N","S G","T"]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 200
# s contains only upper case English letters.
# It's guaranteed that there is only one space between 2 words.
# 
#

# @lc code=start
class Solution:
    def printVertically(self, s: str) -> List[str]:
        words, res = s.split(' '), []
        n = max([len(w) for w in words])
        for i in range(n):
            temp = []
            for w in words:
                if len(w) > i:
                    temp.append(w[i])
                else: 
                    temp.append(' ')
            while temp[-1] == ' ':
                temp.pop()
            res.append(''.join(temp))
        return res
# @lc code=end

