#
# @lc app=leetcode id=1054 lang=python3
#
# [1054] Distant Barcodes
#
# https://leetcode.com/problems/distant-barcodes/description/
#
# algorithms
# Medium (41.27%)
# Likes:    264
# Dislikes: 16
# Total Accepted:    12.4K
# Total Submissions: 30.2K
# Testcase Example:  '[1,1,1,2,2,2]'
#
# In a warehouse, there is a row of barcodes, where the i-th barcode is
# barcodes[i].
# 
# Rearrange the barcodes so that no two adjacent barcodes are equal.  You may
# return any answer, and it is guaranteed an answer exists.
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,1,1,2,2,2]
# Output: [2,1,2,1,2,1]
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,1,1,1,2,2,3,3]
# Output: [1,3,1,3,2,1,2,1]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= barcodes.length <= 10000
# 1 <= barcodes[i] <= 10000
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        res, counts = [0]*len(barcodes), collections.Counter(barcodes)
        i, ordered = 0, sorted(list(counts.keys()), key=lambda x: counts[x])[::-1]
        for k in ordered:
            v = counts[k]
            for _ in range(v):
                res[i] = k
                i += 2
                if i >= len(barcodes):
                    i = 1
        return res
# @lc code=end

