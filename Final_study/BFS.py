from collections import deque

def BFS(G:list, start):
    visited = [False for _ in range(len(G))]
    visited[start] = True
    queue = deque()
    queue.append(start)

    while (queue):
        nowNode = queue.popleft()
        print(f"{nowNode}", end=" ")
        for node in G[nowNode]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)

graph = [
    [],
    [2, 3],
    [1, 4],
    [2],
    [1, 2]
]

BFS(graph, 1)
