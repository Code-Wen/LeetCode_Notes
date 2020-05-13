#
# @lc app=leetcode id=640 lang=python3
#
# [640] Solve the Equation
#
# https://leetcode.com/problems/solve-the-equation/description/
#
# algorithms
# Medium (41.44%)
# Likes:    213
# Dislikes: 493
# Total Accepted:    23.2K
# Total Submissions: 55.9K
# Testcase Example:  '"x+5-3+x=6+x-2"'
#
# 
# Solve a given equation and return the value of x in the form of string
# "x=#value". The equation contains only '+', '-' operation, the variable x and
# its coefficient.
# 
# 
# 
# If there is no solution for the equation, return "No solution".
# 
# 
# If there are infinite solutions for the equation, return "Infinite
# solutions".
# 
# 
# If there is exactly one solution for the equation, we ensure that the value
# of x is an integer.
# 
# 
# Example 1:
# 
# Input: "x+5-3+x=6+x-2"
# Output: "x=2"
# 
# 
# 
# Example 2:
# 
# Input: "x=x"
# Output: "Infinite solutions"
# 
# 
# 
# Example 3:
# 
# Input: "2x=x"
# Output: "x=0"
# 
# 
# 
# Example 4:
# 
# Input: "2x+3x-6x=x+2"
# Output: "x=-1"
# 
# 
# 
# Example 5:
# 
# Input: "x=x+2"
# Output: "No solution"
# 
# 
#

# @lc code=start
class Solution:
    def solveEquation(self, equation: str) -> str:
        l = equation.split('=')
        coefLeft, constLeft = self.parse(l[0])
        coefRight, constRight = self.parse(l[1])
        if coefLeft == coefRight:
            if constLeft == constRight: return "Infinite solutions"
            else: return 'No solution'
        else:
            sol = (constRight-constLeft)//(coefLeft - coefRight) 
            return 'x='+str(sol)
        
    def parse(self, s):
        coef, const, ops = 0, 0, {'+', '-'}
        s = s+'+'
        if s[0] == '-':
            sign, i = -1, 1
        else:
            sign, i = 1, 0
        
        temp = ''
        while i < len(s):
            if s[i] not in ops:
                temp += s[i]
            else:
                if temp[-1] == 'x':
                    coef += sign * int(temp[:-1]) if len(temp) > 1 else sign * 1
                else:
                    const += sign * int(temp)
                temp = ''
                sign = -1 if s[i] == '-' else 1
            i += 1
        return coef, const
# @lc code=end

