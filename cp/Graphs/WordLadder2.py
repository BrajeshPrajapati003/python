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
    
    # adj list (graph)
    # word -> all next words reachable in 1 step
    adj = defaultdict(list)

    q = deque([beginWord]) # bfs (only store words, not path here)
    vis = set([beginWord]) # global visited
    found = False

    # BFS PART: build graph of ONLY shortest paths
    while q and not found:
        level_vis = set()
        # IMP: we collect visited nodes of THIS level separately
        # because same word can have multiple parents in same level

        for _ in range(len(q)): # process one level fully
            word = q.popleft()

            # try changing every character
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + ch + word[i+1:]

                    if new_word in wordSet: # valid transformation
                        if new_word not in vis: # if not visited in previous levels
                            if new_word == endWord:
                                found = True
                            
                            # push into queue only once per level
                            if new_word not in level_vis:
                                q.append(new_word)
                                level_vis.add(new_word)

                            # build graph (parent -> child)
                            # NOTE: we still add edge even if already in level_vis
                            adj[word].append(new_word)
        
        # AFTER finishing level -> mark visited
        # ensures shortest path structure
        vis.update(level_vis)
    
    # DFS PART: now graph contains only shortest paths
    # we generate all paths using backtracking
    res = []

    def dfs(path, word):
        if word == endWord: # reached target -> store path
            res.append(path[:])
            return
        
        # explore all next possible words
        for nei in adj[word]:
            path.append(nei)
            dfs(path, nei)
            path.pop() # backtrack
    
    # only run DFS if we found endword
    if found:
        dfs([beginWord], beginWord)

    return res
