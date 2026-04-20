'''
You're given: startGene, endGene, bank (valid genes)
You can change one character at a time
Allowed characters: A, C, G, T
Every intermediate gene must exist in bank
Goal: Return min no. of mutations. If impossible -> -1

Input: start = "AACCGGTT", end   = "AACCGGTA", bank  = ["AACCGGTA"]
Output: 1
'''

# intuition: each gene = node, 1 mutation = edge, find shortest path -> bfs

# This is a shortest path problem in an unweighted graph where each gene is a node and edges represent valid mutations, so we use BFS.

from collections import deque
import ast

def minMutation(startGene, endGene, bank):
    bankSet = set(bank)

    # if end not present -> impossible
    if endGene not in bankSet:
        return -1
    
    q = deque([(startGene, 0)]) # (current gene, steps)
    vis = set([startGene])

    while q:
        gene, steps = q.popleft()

        # reached target
        if gene == endGene:
            return steps
        
        # try all possible mutations
        for i in range(len(gene)):
            for ch in ['A', 'C', 'G', 'T']:

                new_gene = gene[:i] + ch + gene[i+1:]

                if new_gene in vis or new_gene not in bankSet:
                    continue

                vis.add(new_gene)
                q.append((new_gene, steps + 1))
        
    return -1

startGene = input()
endGene = input()
bank = ast.literal_eval(input()) # [input().strip()]

print(minMutation(startGene, endGene, bank))
