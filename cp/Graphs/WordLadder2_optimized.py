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
from collections import defaultdict, deque

def findLadders(beginWord, endWord, wordList):

    wordSet = set(wordList)
    if endWord not in wordSet:
        return []

    parents = defaultdict(list) # child → list of parents
    q = deque([beginWord])
    visited = set([beginWord])
    found = False

    # BFS: build parent map for shortest paths
    while q and not found:

        level_vis = set() # nodes discovered in this level

        for _ in range(len(q)):
            word = q.popleft()

            # try all one-letter transformations
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':

                    if ch == word[i]:
                        continue

                    new_word = word[:i] + ch + word[i+1:]

                    if new_word in wordSet:

                        # only consider nodes not visited in previous levels
                        if new_word not in visited:

                            if new_word == endWord:
                                found = True

                            # push once per level
                            if new_word not in level_vis:
                                q.append(new_word)
                                level_vis.add(new_word)

                            # record parent (important for path reconstruction)
                            parents[new_word].append(word)

        # mark level nodes as visited AFTER level ends
        visited.update(level_vis)

    # DFS: reconstruct all paths
    res = []

    def dfs(word, path):
        if word == beginWord:
            res.append(path[::-1]) # reverse path
            return

        for p in parents[word]:
            dfs(p, path + [p])

    if found:
        dfs(endWord, [endWord])

    return res
