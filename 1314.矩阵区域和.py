#
# @lc app=leetcode.cn id=1314 lang=python3
#
# [1314] 矩阵区域和
#

# @lc code=start
import copy
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        prefixSums = copy.deepcopy(mat)
        rowBlockSums, res = copy.deepcopy(mat), copy.deepcopy(mat)
        m,n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(1,n):
                prefixSums[i][j] += prefixSums[i][j-1]
        for i in range(m):
            for j in range(n):
                rightSum = prefixSums[i][j+K] if j+K<n else prefixSums[i][n-1]
                leftSum = prefixSums[i][j-K-1] if j-K > 0 else 0
                rowBlockSums[i][j] = rightSum-leftSum
        for i in range(m):
            for j in range(n):
                res[i][j] = sum([rowBlockSums[l][j] for l in range(max(0, i-K), min(m-1,i+K)+1)])
        return res
# @lc code=end

