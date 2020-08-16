
# 484. Find Permutation
# [Medium]
# By now, you are given a secret signature consisting of character 'D' and 'I'. 'D' represents a decreasing relationship between two numbers, 'I' represents an increasing relationship between two numbers. And our secret signature was constructed by a special integer array, which contains uniquely all the different number from 1 to n (n is the length of the secret signature plus 1). For example, the secret signature "DI" can be constructed by array [2,1,3] or [3,1,2], but won't be constructed by array [3,2,4] or [2,1,3,4], which are both illegal constructing special string that can't represent the "DI" secret signature.

# On the other hand, now your job is to find the lexicographically smallest permutation of [1, 2, ... n] could refer to the given secret signature in the input.

# Example 1:
# Input: "I"
# Output: [1,2]
# Explanation: [1,2] is the only legal initial spectial string can construct secret signature "I", where the number 1 and 2 construct an increasing relationship.
# Example 2:
# Input: "DI"
# Output: [2,1,3]
# Explanation: Both [2,1,3] and [3,1,2] can construct the secret signature "DI", 
# but since we want to find the one with the smallest lexicographical permutation, you need to output [2,1,3]
# Note:

# The input string will only contain the character 'D' and 'I'.
# The length of input string is a positive integer and will not exceed 10,000

class Solution:
    def findPermutation(self, s: str) -> List[int]:
    
        def simplePermutation(prev, inc, dec):
            """
            Return a list of unique numbers from
            prev+1 to prev+inc+dec inclusive, such that the first inc steps are increasing
            followed by dec number of decreasing steps
            """
            if inc > 1:
                return [i for i in range(prev+1, prev+inc)]+[prev+inc+dec]+[j for j in range(prev+dec+inc-1, prev+inc-1,-1)]
            else:
                return [prev+inc+dec]+[j for j in range(prev+inc+dec-1, prev,-1)]
        
        prev, pos, inc, dec = 0, 0, 0, 0
        while pos < len(s) and s[pos] == 'D':
            pos += 1
            dec += 1
        if dec:
            res, restart, inc, dec, prev = [i for i in range(dec+1,0,-1)], False, 0, 0, dec+1
        else:
            res, restart, prev = [1], False, 1
        while pos < len(s):
            if s[pos] == 'I':
                if restart:
                    res += simplePermutation(prev, inc, dec)
                    prev += inc+dec
                    inc, dec, restart = 1, 0, False
                else:
                    inc += 1
            else:
                dec += 1
                restart = True
            pos += 1
        if inc:
            res += simplePermutation(prev, inc, dec) 
        return res
        