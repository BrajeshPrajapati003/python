from typing import List

class Solution:

    def findCircleNum(self, adj: List[List[int]]) -> int:
        n = len(adj)
        count = 0

        for i in range(n):
            if adj[i][i] == 1:   # not visited
                self.dfs(adj, i)
                count += 1

        return count


    def dfs(self, adj, node):
        # mark node as visited
        adj[node][node] = 0

        for j in range(len(adj)):
            if adj[node][j] == 1:
                # remove connection BOTH sides
                adj[node][j] = 0
                adj[j][node] = 0

                self.dfs(adj, j)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
sol = Solution()
print(sol.findCircleNum(graph))

# ! GRID PROBLEMS -> modify cell is enough
# ! GRAPH PROBLEMS -> must handle edges or use visited
