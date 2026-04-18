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

# idea: start BFS from beginWord AND endWord
# search space reduces exponentially
# pattern: Bi-directional BFS; TC: O(n/2 * L * 26) -> much faster

def ladderLength(beginWord, endWord, wordList):

    wordSet = set(wordList) # for O(1) lookup

    # if target not present -> impossible
    if endWord not in wordSet:
        return 0

    # start BFS from both ends
    beginSet = {beginWord}
    endSet = {endWord}

    steps = 1 # initial level (beginWord)

    while beginSet:

        # always expand smaller set -> optimization
        if len(beginSet) > len(endSet):
            beginSet, endSet = endSet, beginSet

        nextSet = set() # next level words

        for word in beginSet:

            # try changing each character
            for i in range(len(word)):

                for ch in 'abcdefghijklmnopqrstuvwxyz':

                    # generate new transformed word
                    new_word = word[:i] + ch + word[i+1:]

                    # if both searches meet -> shortest path found
                    if new_word in endSet:
                        return steps + 1
                    
                    # if valid & not visited yet
                    if new_word in wordSet:
                        nextSet.add(new_word) # add to next level
                        wordSet.remove(new_word) # mark visited
        
        # move to next level
        beginSet = nextSet
        steps += 1
    
    return 0 # no transformation possible

#! Basic BFS → try all (TLE)
#! Pattern BFS → jump smarter (faster) 
#! Bidirectional-BFS → meet in middle (fastest)
