#
# @lc app=leetcode id=1233 lang=python3
#
# [1233] Remove Sub-Folders from the Filesystem
#
# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/description/
#
# algorithms
# Medium (59.60%)
# Likes:    228
# Dislikes: 40
# Total Accepted:    19.4K
# Total Submissions: 32.3K
# Testcase Example:  '["/a","/a/b","/c/d","/c/d/e","/c/f"]'
#
# Given a list of folders, remove all sub-folders in those folders and return
# in any order the folders after removing.
# 
# If a folder[i] is located within another folder[j], it is called a sub-folder
# of it.
# 
# The format of a path is one or more concatenated strings of the form: /
# followed by one or more lowercase English letters. For example, /leetcode and
# /leetcode/problems are valid paths while an empty string and / are not.
# 
# 
# Example 1:
# 
# 
# Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
# Output: ["/a","/c/d","/c/f"]
# Explanation: Folders "/a/b/" is a subfolder of "/a" and "/c/d/e" is inside of
# folder "/c/d" in our filesystem.
# 
# 
# Example 2:
# 
# 
# Input: folder = ["/a","/a/b/c","/a/b/d"]
# Output: ["/a"]
# Explanation: Folders "/a/b/c" and "/a/b/d/" will be removed because they are
# subfolders of "/a".
# 
# 
# Example 3:
# 
# 
# Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
# Output: ["/a/b/c","/a/b/ca","/a/b/d"]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= folder.length <= 4 * 10^4
# 2 <= folder[i].length <= 100
# folder[i] contains only lowercase letters and '/'
# folder[i] always starts with character '/'
# Each folder name is unique.
# 
# 
#

# @lc code=start
class Solution:

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        lst = [f[1:].split('/') for f in folder]
        trie = Trie()
        for words in lst:
            trie.insert(words)
        
        return trie.getPrefix()

        

        
        
        
class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie:
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, words):
        node = self.root
        for w in words:
            node = node.children[w]
        node.isWord = True
    
    def getPrefix(self):
        res, queue = [], collections.deque([(self.root,'')])
        while queue:
            node, path = queue.popleft()
            if node.isWord:
                res.append(path)
                continue
            for w in node.children:
                queue.append((node.children[w], path+'/'+w))
        return res
# @lc code=end

