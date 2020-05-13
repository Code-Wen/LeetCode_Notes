
# 742. Closest Leaf in a Binary Tree
# Medium

# Given a binary tree where every node has a unique value, and a target key k, find the value of the nearest leaf node to target k in the tree.

# Here, nearest to a leaf means the least number of edges travelled on the binary tree to reach any leaf of the tree. Also, a node is called a leaf if it has no children.

# In the following examples, the input tree is represented in flattened form row by row. The actual root tree given will be a TreeNode object.

# Example 1:

# Input:
# root = [1, 3, 2], k = 1
# Diagram of binary tree:
#           1
#          / \
#         3   2

# Output: 2 (or 3)

# Explanation: Either 2 or 3 is the nearest leaf node to the target of 1.
# Example 2:

# Input:
# root = [1], k = 1
# Output: 1

# Explanation: The nearest leaf node is the root node itself.
# Example 3:

# Input:
# root = [1,2,3,4,null,null,null,5,null,6], k = 2
# Diagram of binary tree:
#              1
#             / \
#            2   3
#           /
#          4
#         /
#        5
#       /
#      6

# Output: 3
# Explanation: The leaf node with value 3 (and not the leaf node with value 6) is nearest to the node with value 2.
# Note:
# 1. root represents a binary tree with at least 1 node and at most 1000 nodes.
# 2. Every node has a unique node.val in range [1, 1000].
# 3. There exists some node in the given binary tree for which node.val == k.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        # Traverse the tree once to form the undirected graph
        # and identify the leaves
        # Then use BFS to find the nearest leave for k
        edges, leaves = self.traverse(root)
        
        def bfs(start):
            q, seen = collections.deque([start]), {start}
            while q:
                node = q.popleft()
                if node in leaves: return node
                else:
                    for i in edges[node]:
                        if i not in seen:
                            q.append(i)
                            seen.add(i)
        return bfs(k)
    
    def traverse(self, root):
        edges = collections.defaultdict(list)
        stack, leaves = [root], set()
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                leaves.add(node.val)
            else:
                if node.left:
                    stack.append(node.left)
                    edges[node.val].append(node.left.val)
                    edges[node.left.val].append(node.val)
                if node.right:
                    stack.append(node.right)
                    edges[node.val].append(node.right.val)
                    edges[node.right.val].append(node.val)
        return edges, leaves