'''
Given: beginWord, endWord, wordList
You can change one letter at a time
Each intermediate word must exist in wordList

Goal: Find the shortest transformation sequence length

Input: 
    beginWord = "hit", end = "cog"
    WordList = ["hot", "dot", "dog", "lot", "log", "cog"]
Output: 5 (path: hit -> hot -> dot -> dog -> cog)
'''

# idea: This is shortest path in graph; each word = node, edge = 1 letter difference
# Intuition: At each step: try changing each character -> generate neighbors

from collections import deque

def ladderLength(beginWord, endWord, wordList):

    wordSet = set(wordList) # for fast lookups

    if endWord not in wordSet:
        return 0
    
    q = deque([(beginWord, 1)]) # (word, level)

    while q:
        word, steps = q.popleft()

        if word == endWord:
            return steps
        
        # try all possible transformations
        for i in range(len(word)):
            for ch in 'abcdefghijklmnopqrstuvwxyz':

                new_word = word[:i] + ch + word[i+1:]

                if new_word in wordSet:
                    q.append((new_word, steps + 1))
                    wordSet.remove(new_word) # avoid revisiting otherwise infinite loop
    
    return 0


#! We can use bidirectional BFS to reduce search space by half, 
#! or use pattern mapping to avoid generating all possible transformations.
