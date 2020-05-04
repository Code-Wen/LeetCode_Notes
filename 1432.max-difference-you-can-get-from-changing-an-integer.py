#
# @lc app=leetcode id=1432 lang=python3
#
# [1432] Max Difference You Can Get From Changing an Integer
#
# https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/description/
#
# algorithms
# Medium (41.77%)
# Likes:    34
# Dislikes: 40
# Total Accepted:    5.1K
# Total Submissions: 12.2K
# Testcase Example:  '555'
#
# You are given an integer num. You will apply the following steps exactly two
# times:
# 
# 
# Pick a digit x (0 <= x <= 9).
# Pick another digit y (0 <= y <= 9). The digit y can be equal to x.
# Replace all the occurrences of x in the decimal representation of num by
# y.
# The new integer cannot have any leading zeros, also the new integer cannot be
# 0.
# 
# 
# Let a and b be the results of applying the operations to num the first and
# second times, respectively.
# 
# Return the max difference between a and b.
# 
# 
# Example 1:
# 
# 
# Input: num = 555
# Output: 888
# Explanation: The first time pick x = 5 and y = 9 and store the new integer in
# a.
# The second time pick x = 5 and y = 1 and store the new integer in b.
# We have now a = 999 and b = 111 and max difference = 888
# 
# 
# Example 2:
# 
# 
# Input: num = 9
# Output: 8
# Explanation: The first time pick x = 9 and y = 9 and store the new integer in
# a.
# The second time pick x = 9 and y = 1 and store the new integer in b.
# We have now a = 9 and b = 1 and max difference = 8
# 
# 
# Example 3:
# 
# 
# Input: num = 123456
# Output: 820000
# 
# 
# Example 4:
# 
# 
# Input: num = 10000
# Output: 80000
# 
# 
# Example 5:
# 
# 
# Input: num = 9288
# Output: 8700
# 
# 
# 
# Constraints:
# 
# 
# 1 <= num <= 10^8
# 
# 
#

# @lc code=start
class Solution:
    def maxDiff(self, num: int) -> int:
        original = list(str(num))
        
        i1, i2 = 0, 1
        while i1 < len(original) and original[i1] == '9':
            i1 += 1
        toBeReplaced1 = original[i1] if i1 < len(original) else ''
        toReplace1 = '9'
    
        if original[0] != '1':
            toBeReplaced2 = original[0]
            toReplace2 = '1'
        else:
            while i2 < len(original) and (original[i2] == '0' or original[i2]=='1'):
                i2 += 1
            if i2 < len(original):
                toBeReplaced2, toReplace2 = original[i2], '0'
            else:
                toBeReplaced2, toReplace2 = '9', '0'
                
        def getReplacedNum(toBeReplaced, toReplace):
            s = ''
            for l in original:
                if l == toBeReplaced:
                    s += toReplace
                else:
                    s += l
            return int(s)
        
        large, small = getReplacedNum(toBeReplaced1, toReplace1), getReplacedNum(toBeReplaced2, toReplace2)
        return large-small
# @lc code=end

