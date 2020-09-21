#
# @lc app=leetcode id=1291 lang=python3
#
# [1291] Sequential Digits
#
# https://leetcode.com/problems/sequential-digits/description/
#
# algorithms
# Medium (53.35%)
# Likes:    302
# Dislikes: 35
# Total Accepted:    19.3K
# Total Submissions: 34.4K
# Testcase Example:  '100\n300'
#
# An integer has sequential digits if and only if each digit in the number is
# one more than the previous digit.
# 
# Return a sorted list of all the integers in the range [low, high] inclusive
# that have sequential digits.
# 
# 
# Example 1:
# Input: low = 100, high = 300
# Output: [123,234]
# Example 2:
# Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]
# 
# 
# Constraints:
# 
# 
# 10 <= low <= high <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        S = "123456789"
        min_len, max_len = len(str(low)), len(str(high))
        res = []
        for length in range(min_len, max_len+1):
            for i in range(10):
                j = i + length
                if j == 10: break
                num = int(S[i:j])
                if low <= num <= high:
                    res.append(num)
                
        return res
# @lc code=end

