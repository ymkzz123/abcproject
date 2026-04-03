def dfs(v):
    visited[v] = True
    print(v, end=' ')    
    for i in g[v]:
        if not visited[i]:
            dfs(i)
            
            
N = int(input())
visited = [False]*(N+1)
g = [list(map(int, input().split())) for _ in range(N)]
res = 0


dfs(1)
