#
# @lc app=leetcode id=689 lang=python3
#
# [689] Maximum Sum of 3 Non-Overlapping Subarrays
#
# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/description/
#
# algorithms
# Hard (45.41%)
# Likes:    801
# Dislikes: 47
# Total Accepted:    35.9K
# Total Submissions: 79.1K
# Testcase Example:  '[1,2,1,2,6,7,5,1]\n2'
#
# In a given array nums of positive integers, find three non-overlapping
# subarrays with maximum sum.
# 
# Each subarray will be of size k, and we want to maximize the sum of all 3*k
# entries.
# 
# Return the result as a list of indices representing the starting position of
# each interval (0-indexed). If there are multiple answers, return the
# lexicographically smallest one.
# 
# Example:
# 
# 
# Input: [1,2,1,2,6,7,5,1], 2
# Output: [0, 3, 5]
# Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting
# indices [0, 3, 5].
# We could have also taken [2, 1], but an answer of [1, 3, 5] would be
# lexicographically larger.
# 
# 
# 
# 
# Note:
# 
# 
# nums.length will be between 1 and 20000.
# nums[i] will be between 1 and 65535.
# k will be between 1 and floor(nums.length / 3).
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        """
        Idea: for each choice of middle index `mid`, find the index on the left with max k-sums and the index on the right with max k-sums.
        If these three indices give three subarrays with larger sum, update.

        Time: O(N) Space: O(N)
        Issue: Hard to generalize to arbitrary number of subarrays.
        """

        kSums =  [0] * (len(nums)-k+1)
        kSums[0] = sum(nums[:k])
        for i in range(1, len(kSums)):
            kSums[i] = kSums[i-1]-nums[i-1]+nums[i+k-1]
        
        left, right = [0]*len(kSums), [0]*len(kSums)
        best  = kSums[0]
        for i in range(1,len(left)):
            if kSums[i] > best:
                left[i] = i
                best = kSums[i]
            else:
                left[i] = left[i-1]

        best, right[-1] = kSums[-1], len(right)-1
        for i in range(len(right)-2, -1,-1):
            if kSums[i] >= best:
                right[i] = i
                best = kSums[i]
            else:
                right[i] = right[i+1]
        
        threeSum, res = 0, [0, k, 2*k]
        for mid in range(k, len(nums)-2*k+1):
            temp = kSums[left[mid-k]]+kSums[mid]+kSums[right[mid+k]]
            if temp > threeSum:
                threeSum = temp
                res = [left[mid-k], mid, right[mid+k]]
        return res

    def maxSumOfNSubarrays(self, nums: List[int], k: int, N: int) -> List[int]: 
        """
        nums: input array
        k: length of each subarray
        N: number of subarrays

        Return: minimal indices of starting positions of N non-overlapping subarrays with max sum.
        """
        # Motivation: https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/discuss/203666/python-sliding-windows-O(n)O(1)
        # This is the generalized version of the above solution.
        if len(nums) < k*N:
            return 'Impossible to find enough non-overlapping subarrays!'

        d = {}
        tempSum = 0
        for i in range(1, N+1):
            d['w'+str(i)] = sum(nums[(i-1)*k:i*k])
            tempSum += d['w'+str(i)]
            d['max'+str(i)+'sum'] = tempSum
            d['max'+str(i)+'sumIdx'] = [k*j for j in range(i)]
        d['max0sum'], d['max0sumIdx'] = 0, []

        for i in range(1, len(nums)-N*k+1):
            for j in range(1, N+1):
                d['w'+str(j)] += nums[i-1+k*j]-nums[i-1+k*(j-1)]
            
            for j in range(1, N+1):
                if d['max'+str(j-1)+'sum'] + d['w'+str(j)] > d['max'+str(j)+'sum']:
                    tempSum += d['w'+str(j)]
                    d['max'+str(j)+'sum'] = d['max'+str(j-1)+'sum'] + d['w'+str(j)]
                    d['max'+str(j)+'sumIdx'] = d['max'+str(j-1)+'sumIdx'] + [i+(j-1)*k]
        return d['max'+str(N)+'sumIdx']

        
        


        



# @lc code=end

