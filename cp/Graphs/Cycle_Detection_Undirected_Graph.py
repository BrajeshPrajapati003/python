'''
Detect cycle in an undirected graph
'''
def hasCycle(graph, n):
    vis = [False]*n

    for i in range(n):
        if not vis[i]:
            if dfs(graph, i, -1, vis):
                return True
            
    return False

def dfs(graph, node, parent, vis):
    vis[node] = True

    # if we visit a node again & it's not the parent -> cycle
    # u-v-u (back edge to parent) != cycle
    # u-v-x-u (back to other node) = cycle
    for nei in graph[node]:
        if not vis[nei]:
            if dfs(graph, nei, node, vis):
                return True
        elif nei != parent:
            return True # cycle found
    
    return False
