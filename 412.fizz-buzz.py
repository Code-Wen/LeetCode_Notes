#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#
# https://leetcode.com/problems/fizz-buzz/description/
#
# algorithms
# Easy (62.30%)
# Likes:    957
# Dislikes: 1287
# Total Accepted:    365.1K
# Total Submissions: 580.9K
# Testcase Example:  '1'
#
# Write a program that outputs the string representation of numbers from 1 to
# n.
# 
# But for multiples of three it should output “Fizz” instead of the number and
# for the multiples of five output “Buzz”. For numbers which are multiples of
# both three and five output “FizzBuzz”.
# 
# Example:
# 
# n = 15,
# 
# Return:
# [
# ⁠   "1",
# ⁠   "2",
# ⁠   "Fizz",
# ⁠   "4",
# ⁠   "Buzz",
# ⁠   "Fizz",
# ⁠   "7",
# ⁠   "8",
# ⁠   "Fizz",
# ⁠   "Buzz",
# ⁠   "11",
# ⁠   "Fizz",
# ⁠   "13",
# ⁠   "14",
# ⁠   "FizzBuzz"
# ]
# 
# 
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = [None]*n
        three, five = 1, 1
        for i in range(n):
            if not three and not five:
                res[i] = 'FizzBuzz'
            elif not three and five:
                res[i] = 'Fizz'
            elif three and not five:
                res[i] = 'Buzz'
            else:
                res[i] = str(i+1)
            three = (three+1)%3
            five = (five+1)%5
        return res
# @lc code=end

