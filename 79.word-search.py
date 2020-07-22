#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (34.74%)
# Likes:    3886
# Dislikes: 190
# Total Accepted:    489.5K
# Total Submissions: 1.4M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given a 2D board and a word, find if the word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cell, where
# "adjacent" cells are those horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
# 
# Example:
# 
# 
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
# 
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
# 
# 
# 
# Constraints:
# 
# 
# board and word consists only of lowercase and uppercase English letters.
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3
# 
# 
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if not board or not board[0]:
            return False
        
        def dfs(B, i, j, word, k):
            '''
            Search word in the given board B starting at (i,j). Return True if able to
            find the word[k:].
            '''
            if k >= len(word):
                return True
            m, n = len(B), len(B[0])
            if i >= m or j >= n or i<0 or j<0 or B[i][j]!=word[k]:
                return False
            temp = B[i][j]
            B[i][j] = None
            res = dfs(B,i+1,j, word, k+1) or dfs(B,i,j+1, word, k+1) or dfs(B,i-1,j, word, k+1) or dfs(B,i,j-1, word, k+1)
            B[i][j] = temp
            return res
        
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if dfs(board, i, j, word, 0):
                    return True
        return False
# @lc code=end

