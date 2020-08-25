#
# @lc app=leetcode id=826 lang=python3
#
# [826] Most Profit Assigning Work
#
# https://leetcode.com/problems/most-profit-assigning-work/description/
#
# algorithms
# Medium (38.56%)
# Likes:    392
# Dislikes: 63
# Total Accepted:    21K
# Total Submissions: 54.4K
# Testcase Example:  '[2,4,6,8,10]\n[10,20,30,40,50]\n[4,5,6,7]'
#
# We have jobs: difficulty[i] is the difficulty of the ith job, and profit[i]
# is the profit of the ith job. 
# 
# Now we have some workers. worker[i] is the ability of the ith worker, which
# means that this worker can only complete a job with difficulty at most
# worker[i]. 
# 
# Every worker can be assigned at most one job, but one job can be completed
# multiple times.
# 
# For example, if 3 people attempt the same job that pays $1, then the total
# profit will be $3.  If a worker cannot complete any job, his profit is $0.
# 
# What is the most profit we can make?
# 
# Example 1:
# 
# 
# Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker =
# [4,5,6,7]
# Output: 100 
# Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get
# profit of [20,20,30,30] seperately.
# 
# Notes:
# 
# 
# 1 <= difficulty.length = profit.length <= 10000
# 1 <= worker.length <= 10000
# difficulty[i], profit[i], worker[i]  are in range [1, 10^5]
# 
# 
#

# @lc code=start
class Solution:
    def maxProfitAssignment1(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # First Solution: use binary search
        # Note that we do NOT assume that more difficult leads to more profit
        jobs = [[0,0]] + sorted([[difficulty[i], profit[i]] for i in range(len(profit))]) 
        for i in range(1, len(jobs)):
            jobs[i][1] = max(jobs[i-1][1], jobs[i][1])
        res, workerCounts = 0, collections.Counter(worker) 
        def binarySearch(n):
            l, r = 0, len(jobs)-1
            while l < r-1:
                
                mid = (l+r)//2
                if jobs[mid][0] > n:
                    r =  mid - 1
                else:
                    l = mid
            return jobs[l][1] if jobs[r][0] > n else jobs[r][1]
                
        for work, count in workerCounts.items():
            res += binarySearch(work)*count
        return res


    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Second Solution: sort workers as well
        jobs = sorted(zip(difficulty, profit))
        res = i =  bestJob = 0
        for skill in sorted(worker):
            while i < len(jobs) and skill >= jobs[i][0]:
                bestJob = max(bestJob, jobs[i][1])
                i += 1
            res += bestJob
        return res



# @lc code=end

