from collections import deque

def shortest_path(V, edges, start, end):
    # edge case
    if start == end:
        return 0
        
    # build adjacency list
    adj_list = {}
    for i in range(V):
        adj_list[i] = []
    
    for edge in edges:
        u = edge[0]
        v = edge[1]
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    # bfs setup
    q = deque()
    q.append(start)
    visited = [False] * V
    visited[start] = True
    dist = {}
    dist[start] = 0
    
    # bfs traversal
    while len(q) > 0:
        node = q.popleft()
        
        # check neighbors
        for nbr in adj_list[node]:
            if visited[nbr] == False:
                visited[nbr] = True
                dist[nbr] = dist[node] + 1
                q.append(nbr)
                
                # found target?
                if nbr == end:
                    return dist[nbr]
    
    # no path found
    return -1

# test case
V = 5
edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]]
start = 0
end = 4
result = shortest_path(V, edges, start, end)
print(result)
