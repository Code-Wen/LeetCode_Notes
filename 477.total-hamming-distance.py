#
# @lc app=leetcode id=477 lang=python3
#
# [477] Total Hamming Distance
#
# https://leetcode.com/problems/total-hamming-distance/description/
#
# algorithms
# Medium (50.32%)
# Likes:    822
# Dislikes: 53
# Total Accepted:    62.3K
# Total Submissions: 123.7K
# Testcase Example:  '[4,14,2]'
#
# The Hamming distance between two integers is the number of positions at which
# the corresponding bits are different.
# 
# Now your job is to find the total Hamming distance between all pairs of the
# given numbers.
# 
# 
# Example:
# 
# Input: 4, 14, 2
# 
# Output: 6
# 
# Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is
# 0010 (just
# showing the four bits relevant in this case). So the answer will be:
# HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 +
# 2 + 2 = 6.
# 
# 
# 
# Note:
# 
# Elements of the given array are in the range of 0  to 10^9
# Length of the array will not exceed 10^4. 
# 
# 
#

# @lc code=start
class Solution:
    def totalHammingDistance_bruteForce(self, nums: List[int]) -> int:
        """
        Brute Force solution
        """
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                res += bin(nums[i]^nums[j]).count('1')
        return res

    def totalHammingDistance(self, nums: List[int]) -> int:
        """
        For each position i, count the frequency ones[i] of ones in nums.
        Total contribution from position i is (len(nums)-ones[i])*ones[i].
        """
        ones, N = collections.defaultdict(int), len(nums)
        for n in nums:
            s = bin(n)[::-1]
            for i in range(0, len(s)):
                if s[i] == '1':
                    ones[i] += 1
        return sum([(N-ones[i])*ones[i] for i in ones])

# @lc code=end

