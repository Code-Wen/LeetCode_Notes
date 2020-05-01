#
# @lc app=leetcode id=1106 lang=python3
#
# [1106] Parsing A Boolean Expression
#
# https://leetcode.com/problems/parsing-a-boolean-expression/description/
#
# algorithms
# Hard (57.76%)
# Likes:    194
# Dislikes: 17
# Total Accepted:    8.7K
# Total Submissions: 15K
# Testcase Example:  '"!(f)"'
#
# Return the result of evaluating a given boolean expression, represented as a
# string.
# 
# An expression can either be:
# 
# 
# "t", evaluating to True;
# "f", evaluating to False;
# "!(expr)", evaluating to the logical NOT of the inner expression expr;
# "&(expr1,expr2,...)", evaluating to the logical AND of 2 or more inner
# expressions expr1, expr2, ...;
# "|(expr1,expr2,...)", evaluating to the logical OR of 2 or more inner
# expressions expr1, expr2, ...
# 
# 
# 
# Example 1:
# 
# 
# Input: expression = "!(f)"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: expression = "|(f,t)"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: expression = "&(t,f)"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: expression = "|(&(t,f,t),!(t))"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= expression.length <= 20000
# expression[i] consists of characters in {'(', ')', '&', '|', '!', 't', 'f',
# ','}.
# expression is a valid expression representing a boolean, as given in the
# description.
# 
# 
#

# @lc code=start
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        ops, d = '&|!', {'f':False, 't':True}
        operators, operands, = [], []
        for l in expression:
            if l in ops:
                operators.append(l)
            elif l == ')':
                op = operators.pop()
                vals = []
                while operands[-1] != '(':
                    vals.append(d[operands.pop()])
                operands.pop()
                if op == '&':
                    value = all(vals)
                elif op == '|':
                    value = any(vals)
                else:
                    value = not vals[0]
                value =  't' if value else 'f'
                operands.append(value)
            elif l == ',': continue
            else:
                operands.append(l)
        return d[operands[0]]
# @lc code=end

