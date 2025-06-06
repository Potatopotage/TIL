"""
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""
import sys

input = sys.stdin.readline

N = int(input())
que = []
for _ in range(1, N + 1):
    command = input().split()

    if command[0] == 'push':
        que.append(int(command[1]))
    if command[0] == 'pop':
        if que:

            print(que.pop(0))
        else:
            print(-1)
    elif command[0] == 'size':

        print(len(que))
    elif command[0] == 'empty':
        if que:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)



"""
1
2
2
0
1
2
-1
0
1
-1
0
3
"""