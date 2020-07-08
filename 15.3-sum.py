#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (26.37%)
# Likes:    7064
# Dislikes: 817
# Total Accepted:    933.6K
# Total Submissions: 3.5M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
# 
# Note:
# 
# The solution set must not contain duplicate triplets.
# 
# Example:
# 
# 
# Given array nums = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        def twoSum(arr, target):
            if len(arr) < 2: return []
            res, d = [], set()
            for n in arr:
                if target - n in d:
                    res += [[target - n, n]]
                d.add(n)
            return res
        # Remove unnecessary duplicates and put nums in sorted order
        counts, arr = collections.Counter(nums), []
        for n in sorted(counts.keys()):
            arr += [n]*min(counts[n], 3)

        # Search through to find all triples 
        res = set()
        for i in range(len(arr)):
            k = arr[i]
            for pair in twoSum(arr[i+1:], -k):
                res.add(tuple([k]+pair))
        return [list(t) for t in res]
# @lc code=end

