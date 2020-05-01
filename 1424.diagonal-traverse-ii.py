#
# @lc app=leetcode id=1424 lang=python3
#
# [1424] Diagonal Traverse II
#
# https://leetcode.com/problems/diagonal-traverse-ii/description/
#
# algorithms
# Medium (37.95%)
# Likes:    140
# Dislikes: 21
# Total Accepted:    7.7K
# Total Submissions: 20.2K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a list of lists of integers, nums, return all elements of nums in
# diagonal order as shown in the below images.
# 
# Example 1:
# 
# 
# 
# 
# Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,4,2,7,5,3,8,6,9]
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
# Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
# 
# 
# Example 3:
# 
# 
# Input: nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
# Output: [1,4,2,5,3,8,6,9,7,10,11]
# 
# 
# Example 4:
# 
# 
# Input: nums = [[1,2,3,4,5,6]]
# Output: [1,2,3,4,5,6]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i].length <= 10^5
# 1 <= nums[i][j] <= 10^9
# There at most 10^5 elements in nums.
# 
# 
#

# @lc code=start
class Solution:
    # def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
    #     """
    #     Brute-force solution. TLE.
    #     """
    #     m, n = len(nums), max([len(row) for row in nums])
    #     res = []
    #     for x in range(m):
    #         y = 0
    #         while x >= 0:
    #             if y < len(nums[x]):
    #                 res[idx] = nums[x][y]
    #                 idx += 1
    #             x, y = x-1, y+1
    #     for y in range(1,n):
    #         x = m - 1
    #         while y < n and x >= 0:
    #             if y < len(nums[x]):
    #                 res[idx] = nums[x][y]
    #                 idx += 1
    #             x, y = x-1, y+1
    #     return res
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        m, n = len(nums), max([len(row) for row in nums])
        diagonals = [[] for i in range(m+n-1)]
        for i, row in enumerate(nums):
            for j, n in enumerate(row):
                diagonals[i+j].append(n)
        return [n for r in diagonals for n in reversed(r)]

# @lc code=end

