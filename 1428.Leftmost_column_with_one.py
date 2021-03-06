"""
A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means the matrix is n * m.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes you're given the binary matrix mat as input in the following four examples. You will not have access the binary matrix directly.


Example 1:
Input: mat = [[0,0],[1,1]]
Output: 0


Example 2:
Input: mat = [[0,0],[0,1]]
Output: 1


Example 3:
Input: mat = [[0,0],[0,0]]
Output: -1

Example 4:
Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
Output: 1
 

Constraints:

1. 1 <= mat.length, mat[i].length <= 100
2. mat[i][j] is either 0 or 1.
3. mat[i] is sorted in a non-decreasing way.
"""


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        """
        Using binary search on each row.
        Time: O(m log n)

        """
        m, n = binaryMatrix.dimensions()
        def binarySearch(i):
            l, r = 0, n-1
            if binaryMatrix.get(i,r) == 0: return n
            while l < r:
                mid = (l+r)//2
                if binaryMatrix.get(i, mid) == 1: 
                    r = mid
                else:
                    l = mid + 1
            return r
        
        res = n
        for i in range(m):
            res = min(res, binarySearch(i))
        return -1 if res == n else res
    
    def leftMostColumnWithOne_withoutBinarySearch(self, binaryMatrix: 'BinaryMatrix') -> int:
        """
        Optimal solution without binary search: O(max(m,n))
        """
        m, n = binaryMatrix.dimensions()
        x, y = 0, n
        while x < m and y - 1 >= 0:
            if binaryMatrix.get(x,y-1) == 1:
                y -= 1
            else:
                x += 1
        return y if y<n else -1