#
# @lc app=leetcode id=1470 lang=python3
#
# [1470] Shuffle the Array
#
# https://leetcode.com/problems/shuffle-the-array/description/
#
# algorithms
# Easy (90.69%)
# Likes:    125
# Dislikes: 15
# Total Accepted:    19.1K
# Total Submissions: 21K
# Testcase Example:  '[2,5,1,3,4,7]\n3'
#
# Given the array nums consisting of 2n elements in the form
# [x1,x2,...,xn,y1,y2,...,yn].
# 
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7] 
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is
# [2,3,5,4,1,7].
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,3,4,4,3,2,1], n = 4
# Output: [1,4,2,3,3,2,4,1]
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,1,2,2], n = 2
# Output: [1,2,1,2]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 500
# nums.length == 2n
# 1 <= nums[i] <= 10^3
# 
#

# @lc code=start
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res, HALF, idxRes = [0]*len(nums), len(nums)//2, 0
        for i in range(HALF):
            res[idxRes], res[idxRes+1] = nums[i], nums[i+HALF]
            idxRes += 2
        return res
# @lc code=end

