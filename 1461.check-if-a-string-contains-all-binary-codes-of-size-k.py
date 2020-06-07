#
# @lc app=leetcode id=1461 lang=python3
#
# [1461] Check If a String Contains All Binary Codes of Size K
#
# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/description/
#
# algorithms
# Medium (41.22%)
# Likes:    71
# Dislikes: 31
# Total Accepted:    6.6K
# Total Submissions: 16.1K
# Testcase Example:  '"00110110"\n2'
#
# Given a binary string s and an integer k.
# 
# Return True if all binary codes of length k is a substring of s. Otherwise,
# return False.
# 
# 
# Example 1:
# 
# 
# Input: s = "00110110", k = 2
# Output: true
# Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They
# can be all found as substrings at indicies 0, 1, 3 and 2 respectively.
# 
# 
# Example 2:
# 
# 
# Input: s = "00110", k = 2
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: s = "0110", k = 1
# Output: true
# Explanation: The binary codes of length 1 are "0" and "1", it is clear that
# both exist as a substring. 
# 
# 
# Example 4:
# 
# 
# Input: s = "0110", k = 2
# Output: false
# Explanation: The binary code "00" is of length 2 and doesn't exist in the
# array.
# 
# 
# Example 5:
# 
# 
# Input: s = "0000000001011100", k = 4
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 5 * 10^5
# s consists of 0's and 1's only.
# 1 <= k <= 20
# 
# 
#

# @lc code=start
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return len({s[i:i+k] for i in range(len(s)-k+1)}) == (1<<k)

    """
    Follow-up by lee215:
    Given a binary string s and an integer k.
    Return True if all binary code of length k is a subsequence of s. Otherwise, return False.
    
    Solution:
    import re
    return len(findall(r"0+1|1+0", s)) >= k
    """
# @lc code=end

