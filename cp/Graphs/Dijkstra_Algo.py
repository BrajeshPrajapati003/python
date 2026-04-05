'''
You're given a graph: edges have weights (cost)
Goal: Find the shortest dist from src to all nodes
'''
import heapq

def dijkstra(graph, n, src):

    # initialize distances
    dist = [float('inf')]*n
    dist[src] = 0

    # min heap -> (dist, node)
    pq = [(0, src)]

    while pq:

        d, node = heapq.heappop(pq)

        # skip outdated entries
        if d > dist[node]:
            continue

        # explore neighbors
        for nei, wt in graph[node]:

            newDist = d + wt

            # relaxation step
            if newDist < dist[nei]:
                dist[nei] = newDist
                heapq.heappush(pq, (newDist, nei))
    
    return dist
