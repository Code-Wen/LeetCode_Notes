#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#
# https://leetcode.com/problems/partition-labels/description/
#
# algorithms
# Medium (76.19%)
# Likes:    2882
# Dislikes: 127
# Total Accepted:    154K
# Total Submissions: 200.4K
# Testcase Example:  '"ababcbacadefegdehijhklij"'
#
# A string S of lowercase English letters is given. We want to partition this
# string into as many parts as possible so that each letter appears in at most
# one part, and return a list of integers representing the size of these
# parts.
# 
# 
# 
# Example 1:
# 
# 
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it
# splits S into less parts.
# 
# 
# 
# 
# Note:
# 
# 
# S will have length in range [1, 500].
# S will consist of lowercase English letters ('a' to 'z') only.
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        counts = collections.Counter(S)
        cur_counts, indices =  {}, []
        for i in range(len(S)):
            l = S[i]
            if l in cur_counts:
                cur_counts[l] -= 1
                
            else:
                if cur_counts:
                    cur_counts[l] = counts[l] - 1
                    
                else:
                    indices.append(i)
                    cur_counts[l] = counts[l] - 1
                    
            if cur_counts[l] == 0:
                    del cur_counts[l]
        res = [indices[i]-indices[i-1] for i in range(1, len(indices))]
        res += [len(S)-indices[-1]]
        return res
# @lc code=end

