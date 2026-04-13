'''
Cycle detection in directed graph using only vis[] (no separate path[])
'''

# idea: instead of: vis[] + path[]
# we use: vis[] = 0 -> not visited, visiting (in curr DFS path), 2  -> visited (fully processed)

# if we reach a node with vis[node] == 1 -> cycle
# because we came back to a node already in curr path

def hasCycleDirected(n, graph):
    vis = [0]*n # [0,1,2]
    # 0 -> not seen, 1 -> exploring (danger zone), 2 -> safe (fully checked)

    def dfs(node):
        # cycle detected
        if vis[node] == 1:
            return True
        
        # already processed -> safe
        if vis[node] == 2:
            return False
        
        # mark as visiting
        vis[node] = 1

        for nei in graph[node]:
            if dfs(nei):
                return True
        
        # mark as fully processed
        vis[node] = 2
        return False
    
    for i in range(n):
        if vis[i] == 0:
            if dfs(i):
                return True
            
    return False
