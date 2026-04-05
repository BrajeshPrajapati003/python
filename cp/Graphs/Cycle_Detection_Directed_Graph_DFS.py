'''
Detect cycle in a directed graph using DFS
'''
def hasCycle(graph, n):

    vis = [False]*n
    path = [False]*n

    # dfs function to detect cycle starting from 'node'
    def dfs(node):

        vis[node] = True # node seen before
        path[node] = True # node currently in recursion stack

        # explore all neighbors
        for nei in graph[node]:

            # neighbor not visited -> go deeper
            if not vis[nei]:
                if dfs(nei): # if cycle found deeper
                    return True
                
            # neighbor already in curr path -> cycle
            elif path[nei]:
                return True
            
        # backtracking step: remove node from curr path
        path[node] = False
        return False
    
    # check for cycle from every node (different components)
    for i in range(n):
        if not vis[i]:
            if dfs(i):
                return True
    
    return False
