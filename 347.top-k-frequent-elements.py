#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (60.30%)
# Likes:    3190
# Dislikes: 215
# Total Accepted:    406.6K
# Total Submissions: 669.4K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given a non-empty array of integers, return the k most frequent elements.
# 
# Example 1:
# 
# 
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# Note: 
# 
# 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is
# the array's size.
# It's guaranteed that the answer is unique, in other words the set of the top
# k frequent elements is unique.
# You can return the answer in any order.
# 
# 
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        freqs = {}
        for n, freq in counts.items():
            freqs[freq] = freqs.get(freq, [])+[n]
        res = []
        for freq in range(len(nums),0,-1):
            if freq in freqs:
                res += freqs[freq]
            if len(res) >= k:
                return res[:k]
# @lc code=end

