#
# @lc app=leetcode id=506 lang=python3
#
# [506] Relative Ranks
#
# https://leetcode.com/problems/relative-ranks/description/
#
# algorithms
# Easy (50.52%)
# Likes:    264
# Dislikes: 545
# Total Accepted:    55.5K
# Total Submissions: 109.8K
# Testcase Example:  '[5,4,3,2,1]'
#
# 
# Given scores of N athletes, find their relative ranks and the people with the
# top three highest scores, who will be awarded medals: "Gold Medal", "Silver
# Medal" and "Bronze Medal".
# 
# Example 1:
# 
# Input: [5, 4, 3, 2, 1]
# Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# Explanation: The first three athletes got the top three highest scores, so
# they got "Gold Medal", "Silver Medal" and "Bronze Medal". For the left two
# athletes, you just need to output their relative ranks according to their
# scores.
# 
# 
# 
# Note:
# 
# N is a positive integer and won't exceed 10,000.
# All the scores of athletes are guaranteed to be unique.
# 
# 
# 
#

# @lc code=start
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        d = {nums[i]:i for i in range(len(nums))}
        rank, res = 1, [None]*len(nums)
        for k in sorted(d.keys(), reverse=True):
            if rank == 1:
                res[d[k]] = 'Gold Medal'
            elif rank == 2:
                res[d[k]] = 'Silver Medal'
            elif rank == 3:
                res[d[k]] = 'Bronze Medal'
            else:
                res[d[k]] = str(rank)
            rank += 1
        return res


# @lc code=end

