#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (41.57%)
# Likes:    2756
# Dislikes: 166
# Total Accepted:    237.9K
# Total Submissions: 564.3K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# Given a string s and a non-empty string p, find all the start indices of p's
# anagrams in s.
# 
# Strings consists of lowercase English letters only and the length of both
# strings s and p will not be larger than 20,100.
# 
# The order of output does not matter.
# 
# Example 1:
# 
# Input:
# s: "cbaebabacd" p: "abc"
# 
# Output:
# [0, 6]
# 
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# 
# 
# 
# Example 2:
# 
# Input:
# s: "abab" p: "ab"
# 
# Output:
# [0, 1, 2]
# 
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
# 
# 
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pattern, n = collections.Counter(p), len(p)
        runningCount = collections.defaultdict(int)
        for l in s[:n]:
            runningCount[l] += 1
        def compare():
            for l in pattern:
                if runningCount[l] != pattern[l]:
                    return False
            return True
        
        res = [0] if compare() else []
            
        for i in range(n, len(s)):
            runningCount[s[i]] += 1
            runningCount[s[i-n]] -= 1
            if compare():
                res.append(i-n+1)
        return res
# @lc code=end

