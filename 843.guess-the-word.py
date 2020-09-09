#
# @lc app=leetcode id=843 lang=python3
#
# [843] Guess the Word
#
# https://leetcode.com/problems/guess-the-word/description/
#
# algorithms
# Hard (46.05%)
# Likes:    598
# Dislikes: 624
# Total Accepted:    53.7K
# Total Submissions: 116.4K
# Testcase Example:  '"acckzz"\n["acckzz","ccbazz","eiowzz","abcczz"]\n10'
#
# This problem is an interactive problem new to the LeetCode platform.
# 
# We are given a word list of unique words, each word is 6 letters long, and
# one word in this list is chosen as secret.
# 
# You may call master.guess(word) to guess a word.  The guessed word should
# have type string and must be from the original list with 6 lowercase
# letters.
# 
# This function returns an integer type, representing the number of exact
# matches (value and position) of your guess to the secret word.  Also, if your
# guess is not in the given wordlist, it will return -1 instead.
# 
# For each test case, you have 10 guesses to guess the word. At the end of any
# number of calls, if you have made 10 or less calls to master.guess and at
# least one of these guesses was the secret, you pass the testcase.
# 
# Besides the example test case below, there will be 5 additional test cases,
# each with 100 words in the word list.  The letters of each word in those
# testcases were chosen independently at random from 'a' to 'z', such that
# every word in the given word lists is unique.
# 
# 
# Example 1:
# Input: secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]
# 
# Explanation:
# 
# master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
# master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6
# matches.
# master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
# master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
# master.guess("abcczz") returns 4, because "abcczz" has 4 matches.
# 
# We made 5 calls to master.guess and one of them was the secret, so we pass
# the test case.
# 
# 
# Note:  Any solutions that attempt to circumvent the judge will result in
# disqualification.
# 
#

# @lc code=start
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        def match(w1, w2):
            return sum([i==j for i, j in zip(w1, w2)])
        
        matched_length = 0
        while matched_length < 6:
            # Get the counts in each position of words in wordlist
            count = [collections.Counter(w[i] for w in wordlist) for i in range(6)]
            # Choose a word from the wordlist which is most likely to be a match
            # according to our count
            guess = max(wordlist, key = lambda w: sum(count[i][c] for i, c in enumerate(w)))
            # Compute the match length of new guess and the secret word
            matched_length = master.guess(guess)
            # Update the wordlist
            wordlist = [w for w in wordlist if match(w, guess) == matched_length]
# @lc code=end

