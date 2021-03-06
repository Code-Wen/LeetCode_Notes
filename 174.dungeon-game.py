#
# @lc app=leetcode id=174 lang=python3
#
# [174] Dungeon Game
#
# https://leetcode.com/problems/dungeon-game/description/
#
# algorithms
# Hard (29.69%)
# Likes:    1579
# Dislikes: 37
# Total Accepted:    103.8K
# Total Submissions: 326.5K
# Testcase Example:  '[[-2,-3,3],[-5,-10,1],[10,30,-5]]'
#
# table.dungeon, .dungeon th, .dungeon td {
# ⁠ border:3px solid black;
# }
# 
# ⁠.dungeon th, .dungeon td {
# ⁠   text-align: center;
# ⁠   height: 70px;
# ⁠   width: 70px;
# }
# 
# The demons had captured the princess (P) and imprisoned her in the
# bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid
# out in a 2D grid. Our valiant knight (K) was initially positioned in the
# top-left room and must fight his way through the dungeon to rescue the
# princess.
# 
# The knight has an initial health point represented by a positive integer. If
# at any point his health point drops to 0 or below, he dies immediately.
# 
# Some of the rooms are guarded by demons, so the knight loses health (negative
# integers) upon entering these rooms; other rooms are either empty (0's) or
# contain magic orbs that increase the knight's health (positive integers).
# 
# In order to reach the princess as quickly as possible, the knight decides to
# move only rightward or downward in each step.
# 
# 
# 
# Write a function to determine the knight's minimum initial health so that he
# is able to rescue the princess.
# 
# For example, given the dungeon below, the initial health of the knight must
# be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN ->
# DOWN.
# 
# 
# 
# 
# -2 (K)
# -3
# 3
# 
# 
# -5
# -10
# 1
# 
# 
# 10
# 30
# -5 (P)
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# The knight's health has no upper bound.
# Any room can contain threats or power-ups, even the first room the knight
# enters and the bottom-right room where the princess is imprisoned.
# 
# 
#

# @lc code=start
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        # It is essential to walk backwards.
        # Even knowing to walking backwards, this problem is still tricky.
        rows, cols = len(dungeon), len(dungeon[0])
        dp = [[float('inf')] * cols for _ in range(rows)]

        def get_min_health(currCell, nextRow, nextCol):
            if nextRow >= rows or nextCol >= cols:
                return float('inf')
            nextCell = dp[nextRow][nextCol]
            # hero needs at least 1 point to survive
            return max(1, nextCell - currCell)

        for row in reversed(range(rows)):
            for col in reversed(range(cols)):
                currCell = dungeon[row][col]

                right_health = get_min_health(currCell, row, col+1)
                down_health = get_min_health(currCell, row+1, col)
                next_health = min(right_health, down_health)

                if next_health != float('inf'):
                    min_health = next_health
                else:
                    min_health = 1 if currCell >= 0 else (1 - currCell)

                dp[row][col] = min_health

        return dp[0][0]
# @lc code=end

