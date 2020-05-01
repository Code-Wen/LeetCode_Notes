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
        self.d = []
        s, L = characters, combinationLength
        def dfs(start, path):
            if len(path) == L:
                self.d.append(path)
            if len(s) - start < L-len(path): return
            for i in range(start, len(s)):
                dfs(i+1, path+s[i])
        dfs(0, '')
        self.d = sorted(self.d)[::-1]
            
        

    def next(self) -> str:
        return self.d.pop()
        

    def hasNext(self) -> bool:
        return len(self.d) > 0
        
        

# class CombinationIterator:
#     """
#     I misunderstood the original problem. And I hate it.
#     Here is the solution for it.
    
#     Example: if input is ('abc', 2), then in this version there are 6 elements:
#     'ab','ac', 'ba', 'bc', 'ca', 'cb'
#     """

#     def __init__(self, characters: str, combinationLength: int):
#         self.letters = characters
#         self.L = combinationLength
#         self.total = 1
#         self.divisors = [1]
#         self.cnt = 0
#         for i in range(combinationLength):
#             self.total *= (len(characters) - i)
#         for i in range(1, len(characters)):
#             self.divisors.append(self.divisors[-1]*i)
#         self.divisors = self.divisors[::-1]
        

#     def next(self) -> str:
#         res = self.get(self.cnt)
#         self.cnt += 1
#         return res
        

#     def hasNext(self) -> bool:
#         return self.cnt < self.total
    
#     def get(self, n) -> str:
#         res = []
#         choices = list(self.letters)
#         for i in range(self.L):
#             div = self.divisors[i]
#             q, n = n // div, n % div
#             res.append(choices[q])
#             choices = choices[:q]+choices[q+1:]
#         return ''.join(res)
            
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

