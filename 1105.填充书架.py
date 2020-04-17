#
# @lc app=leetcode.cn id=1105 lang=python3
#
# [1105] 填充书架
#
# https://leetcode-cn.com/problems/filling-bookcase-shelves/description/
#
# algorithms
# Medium (49.67%)
# Likes:    44
# Dislikes: 0
# Total Accepted:    2.2K
# Total Submissions: 4.4K
# Testcase Example:  '[[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]\n4'
#
# 附近的家居城促销，你买回了一直心仪的可调节书架，打算把自己的书都整理到新的书架上。
# 
# 你把要摆放的书 books 都整理好，叠成一摞：从上往下，第 i 本书的厚度为 books[i][0]，高度为 books[i][1]。
# 
# 按顺序 将这些书摆放到总宽度为 shelf_width 的书架上。
# 
# 先选几本书放在书架上（它们的厚度之和小于等于书架的宽度 shelf_width），然后再建一层书架。重复这个过程，直到把所有的书都放在书架上。
# 
# 需要注意的是，在上述过程的每个步骤中，摆放书的顺序与你整理好的顺序相同。 例如，如果这里有 5
# 本书，那么可能的一种摆放情况是：第一和第二本书放在第一层书架上，第三本书放在第二层书架上，第四和第五本书放在最后一层书架上。
# 
# 每一层所摆放的书的最大高度就是这一层书架的层高，书架整体的高度为各层高之和。
# 
# 以这种方式布置书架，返回书架整体可能的最小高度。
# 
# 
# 
# 示例：
# 
# 
# 
# 输入：books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelf_width = 4
# 输出：6
# 解释：
# 3 层书架的高度和为 1 + 3 + 2 = 6 。
# 第 2 本书不必放在第一层书架上。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= books.length <= 1000
# 1 <= books[i][0] <= shelf_width <= 1000
# 1 <= books[i][1] <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        # dp[i+1] = min height to stack  books[0:i+1] on the shelf.
        dp = [0]*(len(books)+1)
        dp[1] = books[0][1]
        
        for i in range(1, len(books)):
            temp, height, width = float('inf'), 0, 0
            for j in range(i, -1, -1):
                if width + books[j][0] <= shelf_width:
                    width += books[j][0]
                    height = max(height, books[j][1])
                    temp = min(temp, dp[j]+height)
                else:
                    break
            dp[i+1] = temp
        return dp[-1]
        
# @lc code=end

