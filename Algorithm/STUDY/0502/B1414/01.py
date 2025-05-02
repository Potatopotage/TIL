"""
다솜이의 집에는 N개의 방이 있다
각각의 방에는 모두 한 개의 컴퓨터가 있다
각각의 컴퓨터는 랜선으로 연결되어 있다
어떤 컴퓨터 A와 컴퓨터 B가 있을 때, A와 B가 서로 랜선으로 연결되어 있거나,
또 다른 컴퓨터를 통해서 연결이 되어있으면 서로 통신을 할 수 있다.

다솜이는 집 안에 있는 N개의 컴퓨터를 모두 연결되게 하고 싶다
N개의 컴퓨터가 서로 연결되어 있는 랜선의 길이가 주어질 때,
다솜이가 기부할 수 있는 랜선의 길이의 최대값을 출력하는 프로그램을 작성하시오

랜선의 길이는 a부터 z는 1부터 26을 나타내고 A부터 Z는 27부터 52를 나타낸다
N은 50보다 작거나 같은 자연수이다

다솜이가 기부할 수 있는 랜선 길이의 최대값을 출력한다
만약, 모든 컴퓨터가 연결되어 있지 않으면 -1을 출력한다
"""

# 각 알파벳에 해당되는 가중치 정보를 저장한 딕셔너리
char_dict = {}
for i, c in enumerate(range(ord('a'), ord('z') + 1), start=1):
    char_dict[chr(c)] = i
for i, c in enumerate(range(ord('A'), ord('Z') + 1), start=27):
    char_dict[chr(c)] = i

# 루트를 찾는 함수
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        parent[root_y] = root_x

N = int(input())

lans = [list(input()) for _ in range(N)]

edges = []

for r in range(N):
    for c in range(N):
        if lans[r][c] != '0':
            edges.append((char_dict[lans[r][c]], r, c))

nodes = set()
parent = {}

for value, a, b in edges:
    nodes.update([a, b])

for node in nodes:
    parent[node] = node

edges.sort()
mst = 0
connected = 0

for weight, u, v in edges:
    if find(u) != find(v):
        union(u, v)
        mst += weight
        connected += 1

if connected == N - 1:
    result_sum = 0
    for edge in edges:
        result_sum += edge[0]
    print(result_sum - mst)
else:
    print(-1)



"""
40
-1
0
105
134
"""