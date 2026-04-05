'''
Given a 2D matrix:
    adj[i][j] = 1 -> city is directly connected to city j
    adj[i][j] = 0 -> no direct connection
The matrix represents a graph of cities.
Goal: Find the no. of provinces
A province = a grp of cities that are directly or indirectly connected
'''

from typing import List

class Solution:
    def findCircleNum(self, adj: List[List[int]]) -> int:
        n = len(adj) # no. of nodes (cities)
        vis = [False]*n # visited array
        count = 0 # no. of provinces (connected components)

        # iterate over all nodes
        for i in range(n):
            if not vis[i]: # if node not visited
                self.dfs(adj, i, vis)
                count += 1 # 1 new component found

        return count

    def dfs(self, adj: List[List[int]], node: int, vis: List[bool]):
        vis[node] = True # mark curr node as visited
        n = len(adj)

        # traverse all possible neighbors
        for j in range(n):
            # adj[node][j] == 1 there is a connection
            # not vis[j] -> node j isn't visited yet
            if adj[node][j] == 1 and not vis[j]:
                self.dfs(adj, j, vis)

n = int(input())
graphMatrix = [list(map(int, input().split())) for _ in range(n)]

'''
# create n*n matrix
graphMatrix = [[0]*n for _ in range(n)
# read matrix input
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        graphMatrix[i][j] = row[j]
'''

sol = Solution()
print(sol.findCircleNum(graphMatrix))
