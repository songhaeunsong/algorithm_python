# 1463 바이러스 (실버 3)

import sys
input = sys.stdin.readline

n = int(input())
e = int(input())


graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(e):
    from_node, to_node = map(int, input().split())
    graph[from_node].append(to_node)
    graph[to_node].append(from_node)

infected = 0


def dfs(node):
    global infected
    for next_node in graph[node]:
        if visited[next_node] == 0:
            visited[next_node] = 1
            infected += 1
            dfs(next_node)


visited[1] = 1
dfs(1)

print(infected)
