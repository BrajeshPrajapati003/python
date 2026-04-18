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

# idea: instead of generating all 26 possibilities, we preprocess patterns; Words sharing same patterns are neighbors
# note: instead of try 26 letters every time -> directly jump to valid neighbors

from collections import defaultdict, deque

def ladderLength(beginWord, endWord, wordList):

    if endWord not in wordList:
        return 0
    
    L = len(beginWord)

    # build pattern map
    pattern_map = defaultdict(list)

    for word in wordList:
        for i in range(L):
            pattern = word[:i] + '*' + word[i+1:]
            pattern_map[pattern].append(word)

    # bfs
    q = deque([(beginWord, 1)])
    vis = set([beginWord])

    while q:
        word, steps = q.popleft()

        if word == endWord:
            return steps
        
        for i in range(L):
            pattern = word[:i] + '*' + word[i+1:]

            for nei in pattern_map[pattern]:
                if nei not in vis[nei]:
                    q.append((nei, steps + 1))

            pattern_map[pattern] = [] # avoid reprocessing
    
    return 0
