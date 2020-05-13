#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#
# https://leetcode.com/problems/car-fleet/description/
#
# algorithms
# Medium (42.21%)
# Likes:    398
# Dislikes: 190
# Total Accepted:    24.9K
# Total Submissions: 59K
# Testcase Example:  '12\n[10,8,0,5,3]\n[2,4,1,1,3]'
#
# N cars are going to the same destination along a one lane road.  The
# destination is target miles away.
# 
# Each car i has a constant speed speed[i] (in miles per hour), and initial
# position position[i] miles towards the target along the road.
# 
# A car can never pass another car ahead of it, but it can catch up to it, and
# drive bumper to bumper at the same speed.
# 
# The distance between these two cars is ignored - they are assumed to have the
# same position.
# 
# A car fleet is some non-empty set of cars driving at the same position and
# same speed.  Note that a single car is also a car fleet.
# 
# If a car catches up to a car fleet right at the destination point, it will
# still be considered as one car fleet.
# 
# 
# How many car fleets will arrive at the destination?
# 
# 
# 
# Example 1:
# 
# 
# Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
# Output: 3
# Explanation:
# The cars starting at 10 and 8 become a fleet, meeting each other at 12.
# The car starting at 0 doesn't catch up to any other car, so it is a fleet by
# itself.
# The cars starting at 5 and 3 become a fleet, meeting each other at 6.
# Note that no other cars meet these fleets before the destination, so the
# answer is 3.
# 
# 
# 
# Note:
# 
# 
# 0 <= N <= 10 ^ 4
# 0 < target <= 10 ^ 6
# 0 < speed[i] <= 10 ^ 6
# 0 <= position[i] < target
# All initial positions are different.
# 
#

# @lc code=start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        N, res = len(position), 1
        if not N: return 0
        order = sorted([(position[i], speed[i]) for i in range(N)])
        pos, v = order.pop()
        fleetTime = (target - pos)/v
        while order:
            pos, v = order.pop()
            time = (target - pos)/v
            if time <= fleetTime:
                continue
            else:
                res += 1
                fleetTime = time
        return res
# @lc code=end
