#
# @lc app=leetcode id=273 lang=python3
#
# [273] Integer to English Words
#
# https://leetcode.com/problems/integer-to-english-words/description/
#
# algorithms
# Hard (27.10%)
# Likes:    1108
# Dislikes: 2887
# Total Accepted:    183.7K
# Total Submissions: 676.5K
# Testcase Example:  '123'
#
# Convert a non-negative integer to its english words representation. Given
# input is guaranteed to be less than 2^31 - 1.
# 
# Example 1:
# 
# 
# Input: 123
# Output: "One Hundred Twenty Three"
# 
# 
# Example 2:
# 
# 
# Input: 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
# 
# Example 3:
# 
# 
# Input: 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty
# Seven"
# 
# 
# Example 4:
# 
# 
# Input: 1234567891
# Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven
# Thousand Eight Hundred Ninety One"
# 
# 
#

# @lc code=start
class Solution:
    def numberToWords(self, num: int) -> str:
        if not num: return 'Zero'

        d = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine',20:'Twenty',30:'Thirty', 
        40:'Forty', 50:'Fifty', 60:'Sixty',70:'Seventy', 80:'Eighty', 90:'Ninety',
        11:'Eleven',12:'Twelve',13:'Thirteen', 14:'Fourteen',15:'Fifteen', 16:'Sixteen',
        17:'Seventeen',18:'Eighteen', 19:'Nineteen', 10:'Ten'}
        def translateHundred(n):
            res = ''
            hundreds, n = n//100, n%100
            if hundreds:
                res += d[hundreds]+' Hundred'
            tens = n//10
            if tens:
                if tens > 1:
                    res += ' ' + d[tens*10]
                    n %= 10
                    if n:
                        res += ' '+d[n]
                else:
                    res += ' ' + d[n]
            else:
                if n:
                    res += ' ' + d[n]
            i = 0
            while i < len(res) and res[i] == ' ':
                i += 1
            return res[i:]
        
        res = ''
        billions, num = num//1000000000, num%1000000000
        if billions:
            res += d[billions] + ' Billion'
        millions, num = num//1000000, num%1000000
        if millions:
            res += ' '+translateHundred(millions) + ' Million'
        thousands, num = num//1000, num%1000
        if thousands:
            res += ' ' + translateHundred(thousands) + ' Thousand'
        if num:
            res += ' ' + translateHundred(num)
        i = 0
        while i < len(res) and res[i] == ' ':
            i += 1
        return res[i:]
        

# @lc code=end

