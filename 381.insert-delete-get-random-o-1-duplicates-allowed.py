#
# @lc app=leetcode id=381 lang=python3
#
# [381] Insert Delete GetRandom O(1) - Duplicates allowed
#
# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/description/
#
# algorithms
# Hard (33.72%)
# Likes:    766
# Dislikes: 67
# Total Accepted:    63.3K
# Total Submissions: 187.3K
# Testcase Example:  '["RandomizedCollection","insert","insert","insert","getRandom","remove","getRandom"]\n' +
  '[[],[1],[1],[2],[],[1],[]]'
#
# Design a data structure that supports all following operations in average
# O(1) time.
# Note: Duplicate elements are allowed.
# 
# 
# insert(val): Inserts an item val to the collection.
# remove(val): Removes an item val from the collection if present.
# getRandom: Returns a random element from current collection of elements. The
# probability of each element being returned is linearly related to the number
# of same value the collection contains.
# 
# 
# 
# Example:
# 
# // Init an empty collection.
# RandomizedCollection collection = new RandomizedCollection();
# 
# // Inserts 1 to the collection. Returns true as the collection did not
# contain 1.
# collection.insert(1);
# 
# // Inserts another 1 to the collection. Returns false as the collection
# contained 1. Collection now contains [1,1].
# collection.insert(1);
# 
# // Inserts 2 to the collection, returns true. Collection now contains
# [1,1,2].
# collection.insert(2);
# 
# // getRandom should return 1 with the probability 2/3, and returns 2 with the
# probability 1/3.
# collection.getRandom();
# 
# // Removes 1 from the collection, returns true. Collection now contains
# [1,2].
# collection.remove(1);
# 
# // getRandom should return 1 and 2 both equally likely.
# collection.getRandom();
# 
# 
#

# @lc code=start
class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # self.val_pos[val] (which is a list of indices) contains pos iff self.vals[pos] = val
        self.val_pos = {}  
        self.vals = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        if val not in self.val_pos:
            self.val_pos[val] = {len(self.vals)}
            self.vals.append(val)
            return True
        else:
            self.val_pos[val].add(len(self.vals))
            self.vals.append(val)
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.val_pos: return False
        # Switch the val to the end of the self.vals, then pop it
        if len(self.vals)-1 not in self.val_pos[val]:
            pos = self.val_pos[val].pop()
            val1 = self.vals[-1]
            self.val_pos[val1].add(pos)
            self.val_pos[val1].remove(len(self.vals)-1)
            self.vals[pos] = val1
        else:
            self.val_pos[val] -= {len(self.vals)-1}
        if not self.val_pos[val]:
            del self.val_pos[val]
        self.vals.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        if not self.vals: print("No values in the set!")
        else:
            return self.vals[random.randint(0, len(self.vals)-1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

