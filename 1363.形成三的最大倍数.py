#
# @lc app=leetcode.cn id=1363 lang=python3
#
# [1363] 形成三的最大倍数
#

# @lc code=start
import collections
class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        if not digits: return ''

        counts = collections.Counter(digits)
        remainder = sum(digits)%3
        if remainder == 0: return self.generateNumString(counts)
        if remainder == 1:
            for i in (1,4,7):
                if i in counts:
                    counts[i] -= 1
                    return self.generateNumString(counts)
            
            for i,j  in [(2,2),(2,5),(5,5),(2,8),(5,8),(8,8)]:
                if i == j and counts.get(i,0) >= 2:
                    counts[i] -= 2
                    return self.generateNumString(counts)
                if i != j and i in counts and j in counts:
                    counts[i] -= 1
                    counts[j] -= 1
                    return self.generateNumString(counts)

        if remainder == 2:
            for i in (2, 5, 8):
                if i in counts:
                    counts[i] -= 1
                    return self.generateNumString(counts)
            
            for i,j  in [(1,1),(1,4),(4,4),(1,7),(4,7),(7,7)]:
                if i == j and counts.get(i,0) >= 2:
                    counts[i] -= 2
                    return self.generateNumString(counts)
                if i != j and i in counts and j in counts:
                    counts[i] -= 1
                    counts[j] -= 1
                    return self.generateNumString(counts)



        
    def generateNumString(self, d) -> str:
        '''
        Given a dictionary/counter of available counts.  
        Generate the largest possible integer as a string.
        '''
        res = ''
        for n in range(9, -1, -1):
            if n in d:
                res += str(n)*d[n]
        if not res: return ''
        else:
            return res if res[0] != '0' else '0'




        
# @lc code=end

