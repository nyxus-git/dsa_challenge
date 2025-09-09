def check_cycle(V, edges):
  graph = {i: [] for i in range(V)}

  for edge in edges:
    U, V = edge[0], edge[1]
    graph[U].append(V)
    graph[V].append(U)

  visited = [False for i in range(V)]

  for vertex in range(V):  # Fixed: was "rnage"
    if not visited[vertex]:
      if dfs(vertex, -1, graph, visited):
        return True
    
  return False

def dfs(current, parent, graph, visited):
  visited[current] = True

  for neighbor in graph[current]:  # Fixed: was "grpah"
    if neighbor == parent:
      continue
    
    if visited[neighbor]:
      return True
    
    if dfs(neighbor, current, graph, visited):
      return True
  
  return False

V = 5
edges = [[0,1], [1,2], [2,3], [3,4], [4,0]]
result = check_cycle(V, edges)
print(result)
