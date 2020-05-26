#
# @lc app=leetcode id=930 lang=python3
#
# [930] Binary Subarrays With Sum
#
# https://leetcode.com/problems/binary-subarrays-with-sum/description/
#
# algorithms
# Medium (42.00%)
# Likes:    423
# Dislikes: 22
# Total Accepted:    18.8K
# Total Submissions: 44.7K
# Testcase Example:  '[1,0,1,0,1]\n2'
#
# In an array A of 0s and 1s, how many non-empty subarrays have sum S?
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [1,0,1,0,1], S = 2
# Output: 4
# Explanation: 
# The 4 subarrays are bolded below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# 
# 
# 
# 
# Note:
# 
# 
# A.length <= 30000
# 0 <= S <= A.length
# A[i] is either 0 or 1.
# 
#

# @lc code=start
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        # d[k] = i means that a prefix sum of k appeared first 
        # on the ith location.
        res, d, sum = 0, {0:-1}, 0
        
        for i in range(len(A)):
            sum += A[i]
            if sum >= S: 
                diff = sum - S
                res += d.get(diff+1, i)-d.get(diff, i)
            d.setdefault(sum,i)

        return res

# @lc code=end

