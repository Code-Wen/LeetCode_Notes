#
# @lc app=leetcode id=269 lang=python3
#
# [269] Alien Dictionary
#
# https://leetcode.com/problems/alien-dictionary/description/
#
# algorithms
# Hard (33.31%)
# Likes:    1890
# Dislikes: 377
# Total Accepted:    158K
# Total Submissions: 473.9K
# Testcase Example:  '["wrt","wrf","er","ett","rftt"]'
#
# There is a new alien language which uses the latin alphabet. However, the
# order among letters are unknown to you. You receive a list of non-empty words
# from the dictionary, where words are sorted lexicographically by the rules of
# this new language. Derive the order of letters in this language.
# 
# Example 1:
# 
# 
# Input:
# [
# ⁠ "wrt",
# ⁠ "wrf",
# ⁠ "er",
# ⁠ "ett",
# ⁠ "rftt"
# ]
# 
# Output: "wertf"
# 
# 
# Example 2:
# 
# 
# Input:
# [
# ⁠ "z",
# ⁠ "x"
# ]
# 
# Output: "zx"
# 
# 
# Example 3:
# 
# 
# Input:
# [
# ⁠ "z",
# ⁠ "x",
# ⁠ "z"
# ] 
# 
# Output: "" 
# 
# Explanation: The order is invalid, so return "".
# 
# 
# Note:
# 
# 
# You may assume all letters are in lowercase.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is
# fine.
# 
# 
#

# @lc code=start
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        d = collections.defaultdict(set)
        in_degree = {c:0 for word in words for c in word}
        
        
        def reason(w1, w2):
            """
            Reason the order of letters by checking
            w1 and w2, where w1 is before w2.
            
            In case w1 cannot be before w2, return 0.
            """
            i, n1, n2 = 0, len(w1), len(w2)
            while i < n1 and i < n2:
                if w1[i] != w2[i]:
                    if w2[i] not in d[w1[i]]:
                        d[w1[i]].add(w2[i])
                        in_degree[w2[i]] += 1
                    return 1
                i += 1
            if i == n2 and i < n1:
                return 0
            return 1
        
        # Using a BFS to add letters 
        for i in range(len(words)):
            w1 = words[i]
            for j in range(i+1, len(words)):
                w2 = words[j]
                temp = reason(w1, w2)
                if not temp: return ''
        
        output = []
        queue = collections.deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            c = queue.popleft()
            output.append(c)
            for l in d[c]:
                in_degree[l] -= 1
                if in_degree[l] == 0:
                    queue.append(l)
        return ''.join(output) if len(output) == len(in_degree) else ''
# @lc code=end

