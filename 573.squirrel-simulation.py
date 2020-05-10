# There's a tree, a squirrel, and several nuts. Positions are represented by the cells in a 2D grid. Your goal is to find the minimal distance for the squirrel to collect all the nuts and put them under the tree one by one. The squirrel can only take at most one nut at one time and can move in four directions - up, down, left and right, to the adjacent cell. The distance is represented by the number of moves.
# Example 1:

# Input: 
# Height : 5
# Width : 7
# Tree position : [2,2]
# Squirrel : [4,4]
# Nuts : [[3,0], [2,5]]
# Output: 12

class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        # Let ai, bi be the distance from the i-th nut to 
        # the tree, the squirrel, resp.
        # Then the goal is to find j which minimizes
        # sum_i (2*ai) + bj - aj.
        minDiff, total = float('inf'), 0
        tx,ty, sx,sy = tree[0],tree[1], squirrel[0], squirrel[1]
        for nx, ny in nuts:
            nut2Tree = abs(nx-tx)+abs(ny-ty)
            nut2Squirrel = abs(nx-sx)+abs(ny-sy)
            total += 2 * nut2Tree
            minDiff = min(minDiff, nut2Squirrel-nut2Tree)
        return total + minDiff