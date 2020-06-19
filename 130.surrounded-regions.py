#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (26.41%)
# Likes:    1606
# Dislikes: 638
# Total Accepted:    221.2K
# Total Submissions: 818K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
# surrounded by 'X'.
# 
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
# 
# Example:
# 
# 
# X X X X
# X O O X
# X X O X
# X O X X
# 
# 
# After running your function, the board should be:
# 
# 
# X X X X
# X X X X
# X X X X
# X O X X
# 
# 
# Explanation:
# 
# Surrounded regions shouldn’t be on the border, which means that any 'O' on
# the border of the board are not flipped to 'X'. Any 'O' that is not on the
# border and it is not connected to an 'O' on the border will be flipped to
# 'X'. Two cells are connected if they are adjacent cells connected
# horizontally or vertically.
# 
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) <= 2 or len(board[0]) <= 2: return
        m, n, toCheck, seen, keep = len(board), len(board[0]), [], set(), set()
        for i in range(m):
            if board[i][0] == 'O': 
                toCheck.append((i,0))
                seen.add((i,0))
            if board[i][n-1] == 'O': 
                toCheck.append((i,n-1))
                seen.add((i,n-1))
        for j in range(1,n-1):
            if board[0][j] == "O": 
                toCheck.append((0,j))
                seen.add((0,j))
            if board[m-1][j] == 'O': 
                toCheck.append((m-1,j))
                seen.add((m-1,j))
        def dfs(x,y,m,n):
            stack = [(x,y)]
            while stack:
                i,j = stack.pop()
                keep.add((i,j))
                for i1,j1 in [(i,j+1),(i,j-1),(i+1,j),(i-1,j)]:
                    if 0 <= i1 < m and 0 <= j1 < n and board[i1][j1] == 'O' and (i1,j1) not in seen:
                        seen.add((i1,j1))
                        stack.append((i1,j1))
        for x,y in toCheck:
            dfs(x,y,m,n)
        for i in range(m):
            for j in range(n):
                if (i,j) not in keep: board[i][j] = 'X'
# @lc code=end

