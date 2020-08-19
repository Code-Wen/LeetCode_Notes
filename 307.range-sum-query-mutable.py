#
# @lc app=leetcode id=307 lang=python3
#
# [307] Range Sum Query - Mutable
#
# https://leetcode.com/problems/range-sum-query-mutable/description/
#
# algorithms
# Medium (34.73%)
# Likes:    1370
# Dislikes: 85
# Total Accepted:    111.2K
# Total Submissions: 319.9K
# Testcase Example:  '["NumArray","sumRange","update","sumRange"]\n[[[1,3,5]],[0,2],[1,2],[0,2]]'
#
# Given an integer array nums, find the sum of the elements between indices i
# and j (i ≤ j), inclusive.
# 
# The update(i, val) function modifies nums by updating the element at index i
# to val.
# 
# Example:
# 
# 
# Given nums = [1, 3, 5]
# 
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
# 
# 
# 
# Constraints:
# 
# 
# The array is only modifiable by the update function.
# You may assume the number of calls to update and sumRange function is
# distributed evenly.
# 0 <= i <= j <= nums.length - 1
# 
# 
#

# @lc code=start

# segment tree node
class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None
        
class NumArray:

    def __init__(self, nums: List[int]):
        # helper function to create the tree
        def creatTree(nums, l, r):
            # incorrect case
            if l > r: 
                return None
            # base case: leaf node
            if l == r:
                n = Node(l, r)
                n.total = nums[l]
                return n
            
            mid = (l + r)//2
            root = Node(l,r)
            # build the left and right subtree first
            root.left = creatTree(nums, l, mid)
            root.right = creatTree(nums, mid+1, r)
            # update total
            root.total = root.left.total + root.right.total

            return root
        
        # initialize the data
        self.root = creatTree(nums, 0, len(nums)-1)

    def update(self, i: int, val: int) -> None:
        # helper function to update the tree
        def updateVal(root, i, val):
            # base case: leaf node
            if root.start == root.end:
                root.total = val
                return val
            
            # Otherwise, update left or right subtree.
            # Note that non-leaf nodes always have left and right children
            mid = (root.start +  root.end) //2 

            if i <= mid:
                updateVal(root.left, i, val)
            else:
                updateVal(root.right, i, val)
            
            # propogate the changes to the root total
            root.total = root.left.total + root.right.total
            return root.total

        updateVal(self.root, i, val)

    def sumRange(self, i: int, j: int) -> int:
        # helper function to calculate the range sum
        def rangeSum(root, l, r):
            # case 1: perfect match
            if root.start == l and root.end == r:
                return root.total
            
            mid = (root.start + root.end) // 2
            # case 2: interval falls entirely on the left subtree
            if r <= mid:
                return rangeSum(root.left, l, r)
            # case 3: interval falls entirely on the right subtree
            elif l > mid:
                return rangeSum(root.right, l, r)
            # last case: interval has parts in both subtrees
            else:
                return rangeSum(root.left, l, mid) + rangeSum(root.right, mid+1, r)

        return rangeSum(self.root, i, j)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
# @lc code=end

