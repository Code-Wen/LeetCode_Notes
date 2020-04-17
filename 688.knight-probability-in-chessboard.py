#
# @lc app=leetcode id=688 lang=python3
#
# [688] Knight Probability in Chessboard
#
# https://leetcode.com/problems/knight-probability-in-chessboard/description/
#
# algorithms
# Medium (47.70%)
# Likes:    643
# Dislikes: 149
# Total Accepted:    35.7K
# Total Submissions: 74.8K
# Testcase Example:  '3\n2\n0\n0'
#
# On an NxN chessboard, a knight starts at the r-th row and c-th column and
# attempts to make exactly K moves. The rows and columns are 0 indexed, so the
# top-left square is (0, 0), and the bottom-right square is (N-1, N-1).
# 
# A chess knight has 8 possible moves it can make, as illustrated below. Each
# move is two squares in a cardinal direction, then one square in an orthogonal
# direction.
# 
# 
# 
# 
# 
# 
# 
# Each time the knight is to move, it chooses one of eight possible moves
# uniformly at random (even if the piece would go off the chessboard) and moves
# there.
# 
# The knight continues moving until it has made exactly K moves or has moved
# off the chessboard. Return the probability that the knight remains on the
# board after it has stopped moving.
# 
# 
# 
# Example:
# 
# 
# Input: 3, 2, 0, 0
# Output: 0.0625
# Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight
# on the board.
# From each of those positions, there are also two moves that will keep the
# knight on the board.
# The total probability the knight stays on the board is 0.0625.
# 
# 
# 
# 
# Note:
# 
# 
# N will be between 1 and 25.
# K will be between 0 and 100.
# The knight always initially starts on the board.
# 
# 
#

# @lc code=start
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        if r < 0 or r >= N or c < 0 or c >= N:
            return 0
        
        probs = [[0]*N for _ in range(N)]
        probs[r][c] = 1
        moves = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
        for _ in range(K):
            prev = copy.deepcopy(probs)
            for x in range(N):
                for y in range(N):
                    p = 0
                    for x1, y1 in moves:
                        if 0<=x+x1<N and 0<= y+y1<N:
                            p += prev[x+x1][y+y1]/(8.0)
                    probs[x][y] = p
        return sum([sum(row) for row in probs])





# @lc code=end

