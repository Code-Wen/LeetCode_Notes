#
# @lc app=leetcode id=773 lang=python3
#
# [773] Sliding Puzzle
#
# https://leetcode.com/problems/sliding-puzzle/description/
#
# algorithms
# Hard (59.39%)
# Likes:    749
# Dislikes: 26
# Total Accepted:    41.7K
# Total Submissions: 70.1K
# Testcase Example:  '[[1,2,3],[4,0,5]]'
#
# On a 2x3 board, there are 5 tiles represented by the integers 1 through 5,
# and an empty square represented by 0.
# 
# A move consists of choosing 0 and a 4-directionally adjacent number and
# swapping it.
# 
# The state of the board is solved if and only if the board is
# [[1,2,3],[4,5,0]].
# 
# Given a puzzle board, return the least number of moves required so that the
# state of the board is solved. If it is impossible for the state of the board
# to be solved, return -1.
# 
# Examples:
# 
# 
# Input: board = [[1,2,3],[4,0,5]]
# Output: 1
# Explanation: Swap the 0 and the 5 in one move.
# 
# 
# 
# Input: board = [[1,2,3],[5,4,0]]
# Output: -1
# Explanation: No number of moves will make the board solved.
# 
# 
# 
# Input: board = [[4,1,2],[5,0,3]]
# Output: 5
# Explanation: 5 is the smallest number of moves that solves the board.
# An example path:
# After move 0: [[4,1,2],[5,0,3]]
# After move 1: [[4,1,2],[0,5,3]]
# After move 2: [[0,1,2],[4,5,3]]
# After move 3: [[1,0,2],[4,5,3]]
# After move 4: [[1,2,0],[4,5,3]]
# After move 5: [[1,2,3],[4,5,0]]
# 
# 
# 
# Input: board = [[3,2,4],[1,5,0]]
# Output: 14
# 
# 
# Note:
# 
# 
# board will be a 2 x 3 array as described above.
# board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].
# 
# 
#

# @lc code=start
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        """
        BFS solution.
        """
        def getState(game):
            return ''.join([str(x) for row in game for x in row])
        
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 0:
                    x, y = i, j
        
        def getNextStates(game,x,y):
            m, n =  len(game), len(game[0])
            res = []
            for i,j in [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]:
                if 0<=i<m and 0<=j<n:
                    new_game = copy.deepcopy(game)
                    new_game[i][j], new_game[x][y] = new_game[x][y], new_game[i][j]
                    res.append((new_game, i, j))
            return res
        
        seen, queue = set(), collections.deque([(board, x, y, 0)])
        seen.add(getState(board))
        GOAL = '123450'
        while queue:
            game, x, y, steps = queue.popleft()
             
            if getState(game) == GOAL:
                return steps
            for new_game, i, j in getNextStates(game, x, y):
                new_state = getState(new_game)
                if new_state not in seen:
                    seen.add(new_state)
                    queue.append((new_game, i, j, steps+1))
        return -1
# @lc code=end

