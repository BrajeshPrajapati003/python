'''
Given: beginWord, endWord, wordList
You can change one letter at a time
Each intermediate word must exist in wordList

Goal: Return all shortest transformation sequences

Input: 
    begin = "hit"; end   = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
Output: [
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
'''
from collections import defaultdict

def findLadders(beginWord, endWord, wordList):
    
    wordSet = set(wordList)

    # if endWord not present → no transformation possible
    if endWord not in wordSet:
        return []
    
    # parents map: child → list of parents
    parents = defaultdict(list)

    # current BFS level (start from beginWord)
    level = {beginWord}
    
    # BFS until we find endWord
    # we stop as soon as shortest level containing endWord is found
    while level and endWord not in parents:

        # next level nodes + their parents
        next_level = defaultdict(list)
        
        # remove current level words from wordSet
        # ensures we don't revisit and only keep shortest paths
        for word in level:
            wordSet.discard(word)
        
        # explore all words in current level
        for word in level:

            # try changing each character
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':

                    # generate new transformed word
                    new_word = word[:i] + c + word[i+1:]
                    
                    # if valid transformation
                    if new_word in wordSet:

                        # store parent relationship
                        # new_word can be reached from 'word'
                        next_level[new_word].append(word)
        
        # move to next level
        level = next_level

        # merge next_level into parents map
        for word in next_level:
            parents[word].extend(next_level[word])
    
    # ---------------- DFS PART ----------------
    # build all paths from endWord → beginWord
    
    res = []
    
    def dfs(word, path):

        # reached start → store reversed path
        if word == beginWord:
            res.append(path[::-1])
            return
        
        # go through all parents
        for p in parents[word]:
            dfs(p, path + [p])
    
    # only run DFS if endWord was reached
    if endWord in parents:
        dfs(endWord, [endWord])
    
    return res
