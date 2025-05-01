"""
트리의 지름이란, 트리에서 임이의 두 접의 사리의 거리 중 가장 긴 것을 말한다
트리의 지름을 구하는 프로그램을 작성하시오

트리의 정점의 개수 V
V개의 줄애 걸쳐 간선의 정보
정점번호, 연결된 간선의 정보를 의미하는 정수 2개
하나는 정점 번호, 다른 하나는 그 정점까지의 거리
"""
import sys
input = sys.stdin.readline

V = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    data = list(map(int, input().split()))
    node = data[0]
    index = 1
    while data[index] != -1:
        neighbor = data[index]
        distance = data[index + 1]
        graph[node].append((neighbor, distance))
        index += 2

def dfs(node, accumulated):
    for neighbor, cost in graph[node]:
        if visited[neighbor] == -1:
            visited[neighbor] = accumulated + cost
            dfs(neighbor, accumulated + cost)

visited = [-1] * (V + 1)
visited[1] = 0
dfs(1, 0)


farthest_node = visited.index(max(visited))

visited = [-1] * (V + 1)
visited[farthest_node] = 0
dfs(farthest_node, 0)

print(max(visited))
