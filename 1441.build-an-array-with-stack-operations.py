#
# @lc app=leetcode id=1441 lang=python3
#
# [1441] Build an Array With Stack Operations
#
# https://leetcode.com/problems/build-an-array-with-stack-operations/description/
#
# algorithms
# Easy (69.14%)
# Likes:    71
# Dislikes: 55
# Total Accepted:    12.3K
# Total Submissions: 17.8K
# Testcase Example:  '[1,3]\r\n3\r'
#
# Given an array target and an integer n. In each iteration, you will read a
# number from  list = {1,2,3..., n}.
# 
# Build the target array using the following operations:
# 
# 
# Push: Read a new element from the beginning list, and push it in the
# array.
# Pop: delete the last element of the array.
# If the target array is already built, stop reading more elements.
# 
# 
# You are guaranteed that the target array is strictly increasing, only
# containing numbers between 1 to n inclusive.
# 
# Return the operations to build the target array.
# 
# You are guaranteed that the answer is unique.
# 
# 
# Example 1:
# 
# 
# Input: target = [1,3], n = 3
# Output: ["Push","Push","Pop","Push"]
# Explanation: 
# Read number 1 and automatically push in the array -> [1]
# Read number 2 and automatically push in the array then Pop it -> [1]
# Read number 3 and automatically push in the array -> [1,3]
# 
# 
# Example 2:
# 
# 
# Input: target = [1,2,3], n = 3
# Output: ["Push","Push","Push"]
# 
# 
# Example 3:
# 
# 
# Input: target = [1,2], n = 4
# Output: ["Push","Push"]
# Explanation: You only need to read the first 2 numbers and stop.
# 
# 
# Example 4:
# 
# 
# Input: target = [2,3,4], n = 4
# Output: ["Push","Pop","Push","Push","Push"]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= target.length <= 100
# 1 <= target[i] <= 100
# 1 <= n <= 100
# target is strictly increasing.
# 
# 
#

# @lc code=start
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        n,i, j, ops = len(target), 0, 1, []
        while i < n:
            if j != target[i]:
                ops += ['Push','Pop']
                j += 1
            else:
                ops += ['Push']
                i += 1
                j += 1
        return ops


# @lc code=end

