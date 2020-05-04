#
# @lc app=leetcode id=1438 lang=python3
#
# [1438] Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
#
# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/
#
# algorithms
# Medium (34.64%)
# Likes:    190
# Dislikes: 4
# Total Accepted:    7.4K
# Total Submissions: 19.8K
# Testcase Example:  '[8,2,4,7]\n4'
#
# Given an array of integers nums and an integer limit, return the size of the
# longest continuous subarray such that the absolute difference between any two
# elements is less than or equal to limit.
# 
# In case there is no subarray satisfying the given condition return 0.
# 
# 
# Example 1:
# 
# 
# Input: nums = [8,2,4,7], limit = 4
# Output: 2 
# Explanation: All subarrays are: 
# [8] with maximum absolute diff |8-8| = 0 <= 4.
# [8,2] with maximum absolute diff |8-2| = 6 > 4. 
# [8,2,4] with maximum absolute diff |8-2| = 6 > 4.
# [8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
# [2] with maximum absolute diff |2-2| = 0 <= 4.
# [2,4] with maximum absolute diff |2-4| = 2 <= 4.
# [2,4,7] with maximum absolute diff |2-7| = 5 > 4.
# [4] with maximum absolute diff |4-4| = 0 <= 4.
# [4,7] with maximum absolute diff |4-7| = 3 <= 4.
# [7] with maximum absolute diff |7-7| = 0 <= 4. 
# Therefore, the size of the longest subarray is 2.
# 
# 
# Example 2:
# 
# 
# Input: nums = [10,1,2,4,7,2], limit = 5
# Output: 4 
# Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute
# diff is |2-7| = 5 <= 5.
# 
# 
# Example 3:
# 
# 
# Input: nums = [4,2,2,2,4,4,2,2], limit = 0
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 0 <= limit <= 10^9
# 
#

# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        Use two queues to keep the running indices of min/max values;
        Use left to keep record the left side of the sliding window;
        """
        
        minQ, maxQ = collections.deque([0]), collections.deque([0])
        left, res = 0, 1
        for i in range(1, len(nums)):
            # Slide right the current min val doesn't work
            while minQ and abs(nums[i] - nums[minQ[0]]) > limit:
                left = max(minQ.popleft() + 1, left)
            # Slide right if the current max val doesn't work
            while maxQ and abs(nums[i] - nums[maxQ[0]]) > limit:
                left = max(maxQ.popleft() + 1, left)
            
            # Update the max length
            res = max(res, i+1-left)
            
            # Update the minQ and maxQ
            while maxQ and nums[i] > nums[maxQ[-1]]:
                maxQ.pop()
            maxQ.append(i)
            
            while minQ and nums[i] < nums[minQ[-1]]:
                minQ.pop()
            minQ.append(i)
        return res
# @lc code=end

