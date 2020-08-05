#
# @lc app=leetcode id=211 lang=python3
#
# [211] Add and Search Word - Data structure design
#
# https://leetcode.com/problems/add-and-search-word-data-structure-design/description/
#
# algorithms
# Medium (36.38%)
# Likes:    2056
# Dislikes: 97
# Total Accepted:    208.2K
# Total Submissions: 554K
# Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n' +
  '[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
# Design a data structure that supports the following two operations:
# 
# 
# void addWord(word)
# bool search(word)
# 
# 
# search(word) can search a literal word or a regular expression string
# containing only letters a-z or .. A . means it can represent any one letter.
# 
# Example:
# 
# 
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# 
# 
# Note:
# You may assume that all words are consist of lowercase letters a-z.
# 
#

# @lc code=start
class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        prev,cur = [node], []
        for w in word:
            if w == '.':
                for node in prev:
                    for i in range(ord('a'), ord('z')+1):
                        nxt_node = node.children.get(chr(i))
                        if nxt_node:
                            cur.append(nxt_node)
            else:
                for node in prev:
                    nxt_node = node.children.get(w)
                    if nxt_node:
                        cur.append(nxt_node)
            prev, cur = cur, []
        for node in prev:
            if node.isWord: return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for w in prefix:
            node = node.children.get(w)
            if not node:
                return False
        return True

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.trie.search(word)
        
class WordDictionary1:
    # Second solution: use lengths to index stored words.
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = {0:''}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.words[len(word)] = self.words.get(len(word), [])+[word]

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if len(word) not in self.words:
            return False
        
        for w in self.words[len(word)]:
            match = True
            for i in range(len(word)):
                if word[i] == '.':
                    continue
                else:
                    if word[i] != w[i]:
                        match = False
                        break
            if match == True: return True
        return False



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

