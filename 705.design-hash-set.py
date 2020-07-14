#
# @lc app=leetcode id=705 lang=python3
#
# [705] Design HashSet
#
# https://leetcode.com/problems/design-hashset/description/
#
# algorithms
# Easy (60.39%)
# Likes:    340
# Dislikes: 70
# Total Accepted:    52.6K
# Total Submissions: 86.8K
# Testcase Example:  '["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]\n' +
  '[[],[1],[2],[1],[3],[2],[2],[2],[2]]'
#
# Design a HashSet without using any built-in hash table libraries.
# 
# To be specific, your design should include these functions:
# 
# 
# add(value): Insert a value into the HashSet. 
# contains(value) : Return whether the value exists in the HashSet or not.
# remove(value): Remove a value in the HashSet. If the value does not exist in
# the HashSet, do nothing.
# 
# 
# 
# Example:
# 
# 
# MyHashSet hashSet = new MyHashSet();
# hashSet.add(1);         
# hashSet.add(2);         
# hashSet.contains(1);    // returns true
# hashSet.contains(3);    // returns false (not found)
# hashSet.add(2);          
# hashSet.contains(2);    // returns true
# hashSet.remove(2);          
# hashSet.contains(2);    // returns false (already removed)
# 
# 
# 
# Note:
# 
# 
# All values will be in the range of [0, 1000000].
# The number of operations will be in the range of [1, 10000].
# Please do not use the built-in HashSet library.
# 
# 
#

# @lc code=start
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyRange = 769
        self.bucketArray = [Bucket() for i in range(self.keyRange)]

    def add(self, key: int) -> None:
        bucketIndex = key % self.keyRange
        self.bucketArray[bucketIndex].insert(key)

    def remove(self, key: int) -> None:
        bucketIndex = key % self.keyRange
        self.bucketArray[bucketIndex].delete(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        bucketIndex = key % self.keyRange
        return self.bucketArray[bucketIndex].exists(key)

class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode  

class Bucket:
    def __init__(self):
        # a pseudo head
        self.head = Node(0)

    def insert(self, newValue):
        # if not existed, add the new element to the head.
        if not self.exists(newValue):
            newNode = Node(newValue, self.head.next)
            # set the new head.
            self.head.next = newNode

    def delete(self, value):
        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr.value == value:
                # remove the current node
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def exists(self, value):
        curr = self.head.next
        while curr is not None:
            if curr.value == value:
                # value existed already, do nothing
                return True
            curr = curr.next
        return False



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end

