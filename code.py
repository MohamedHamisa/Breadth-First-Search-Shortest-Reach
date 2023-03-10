from collections import deque, defaultdict

def bfs(n, m, edges, s, cost = 6):
    
    graph = defaultdict(list)
    for u, v in edges:
        graph[u] += [v]
        graph[v] += [u]
    
    res = [-1] * (n+1)
    res[s] = 0
    q = deque([(s, 0)])
    
    while q:
        node, total = q.popleft()
        total += cost
        for i in graph[node]:
            if res[i] == -1:
                q.append((i, total))
                res[i] = total
    
    return res[1:s] + res[s+1:]


