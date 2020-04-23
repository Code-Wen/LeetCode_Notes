#
# @lc app=leetcode id=1286 lang=python3
#
# [1286] Iterator for Combination
#
# https://leetcode.com/problems/iterator-for-combination/description/
#
# algorithms
# Medium (66.37%)
# Likes:    129
# Dislikes: 14
# Total Accepted:    6.6K
# Total Submissions: 9.9K
# Testcase Example:  '["CombinationIterator","next","hasNext","next","hasNext","next","hasNext"]\r\n' +
  '[["abc",2],[],[],[],[],[],[]]\r'
#
# Design an Iterator class, which has:
# 
# 
# A constructor that takes a string characters of sorted distinct lowercase
# English letters and a number combinationLength as arguments.
# A function next() that returns the next combination of length
# combinationLength in lexicographical order.
# A function hasNext() that returns True if and only if there exists a next
# combination.
# 
# 
# 
# 
# Example:
# 
# 
# CombinationIterator iterator = new CombinationIterator("abc", 2); // creates
# the iterator.
# 
# iterator.next(); // returns "ab"
# iterator.hasNext(); // returns true
# iterator.next(); // returns "ac"
# iterator.hasNext(); // returns true
# iterator.next(); // returns "bc"
# iterator.hasNext(); // returns false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= combinationLength <= characters.length <= 15
# There will be at most 10^4 function calls per test.
# It's guaranteed that all calls of the function next are valid.
# 
# 
#

# @lc code=start
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        

    def next(self) -> str:
        

    def hasNext(self) -> bool:
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

