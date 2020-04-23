#
# @lc app=leetcode id=1320 lang=python3
#
# [1320] Minimum Distance to Type a Word Using Two Fingers
#
# https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/description/
#
# algorithms
# Hard (58.88%)
# Likes:    234
# Dislikes: 9
# Total Accepted:    7.5K
# Total Submissions: 12.8K
# Testcase Example:  '"CAKE"'
#
# 
# 
# You have a keyboard layout as shown above in the XY plane, where each English
# uppercase letter is located at some coordinate, for example, the letter A is
# located at coordinate (0,0), the letter B is located at coordinate (0,1), the
# letter P is located at coordinate (2,3) and the letter Z is located at
# coordinate (4,1).
# 
# Given the string word, return the minimum total distance to type such string
# using only two fingers. The distance between coordinates (x1,y1) and (x2,y2)
# is |x1 - x2| + |y1 - y2|. 
# 
# Note that the initial positions of your two fingers are considered free so
# don't count towards your total distance, also your two fingers do not have to
# start at the first letter or the first two letters.
# 
# 
# Example 1:
# 
# 
# Input: word = "CAKE"
# Output: 3
# Explanation: 
# Using two fingers, one optimal way to type "CAKE" is: 
# Finger 1 on letter 'C' -> cost = 0 
# Finger 1 on letter 'A' -> cost = Distance from letter 'C' to letter 'A' = 2 
# Finger 2 on letter 'K' -> cost = 0 
# Finger 2 on letter 'E' -> cost = Distance from letter 'K' to letter 'E' = 1 
# Total distance = 3
# 
# 
# Example 2:
# 
# 
# Input: word = "HAPPY"
# Output: 6
# Explanation: 
# Using two fingers, one optimal way to type "HAPPY" is:
# Finger 1 on letter 'H' -> cost = 0
# Finger 1 on letter 'A' -> cost = Distance from letter 'H' to letter 'A' = 2
# Finger 2 on letter 'P' -> cost = 0
# Finger 2 on letter 'P' -> cost = Distance from letter 'P' to letter 'P' = 0
# Finger 1 on letter 'Y' -> cost = Distance from letter 'A' to letter 'Y' = 4
# Total distance = 6
# 
# 
# Example 3:
# 
# 
# Input: word = "NEW"
# Output: 3
# 
# 
# Example 4:
# 
# 
# Input: word = "YEAR"
# Output: 7
# 
# 
# 
# Constraints:
# 
# 
# 2 <= word.length <= 300
# Each word[i] is an English uppercase letter.
# 
#

# @lc code=start
class Solution:
    def minimumDistance(self, word: str) -> int:
        if len(word) <= 2:
            return 0

        start, cols = ord('A'), 6
        @functools.lru_cache(None)
        def getCoordinates(l):
            n = ord(l)-start
            x, y = n // 6, n % 6
            return x,y

        @functools.lru_cache(None)
        def computeDist(l1, l2):
            x1, y1 = getCoordinates(l1)
            x2, y2 = getCoordinates(l2)
            return abs(x1-x2)+abs(y1-y2)
        # dp[combo] is the current minimal distance
        # if len(combo) == 1: only one finger is used
        # if len(combo) == 2: the last letters for 1st and 2nd finger are combo[0], combo[1]
        # We assume that combo[0] <= combo[1] to avoid repetitions.
        dp = {}
        l1, l2 = word[0], word[1]
        dp[l2] = computeDist(l1,l2)
        l1, l2 = min(l1, l2), max(l1,l2)
        dp[l1+l2] = 0
        for l in word[2:]:
            temp = {}
            for combo in dp:
                if len(combo) == 1:
                    temp[l] = dp[combo]+computeDist(combo,l)
                    l1,l2 = min(combo,l), max(combo,l)
                    newCombo = l1+l2
                    temp[newCombo] = min(temp.get(newCombo, float('inf')), dp[combo])
                else:
                    for i in range(2):
                        l0, l3 = combo[i], combo[(i+1)%2]
                        l1, l2 = min(l, l3), max(l,l3)
                        newCombo = l1+l2
                        temp[newCombo] = min(temp.get(newCombo, float('inf')), dp[combo]+computeDist(l,l0))
            dp = temp
        return min(dp.values())


# @lc code=end

