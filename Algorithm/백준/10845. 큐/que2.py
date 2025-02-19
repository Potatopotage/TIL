from collections import deque
import sys

sys.stdin = open('input.txt', 'r')

N = int(input())

dq = deque()
for _ in range(N):
    command = list(input().split())

    if command[0] == 'push':
        dq.append(command[1])

    elif command[0] == 'pop':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(dq))
    elif command[0] == 'empty':
        if command:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if dq:
            print(dq[-1])
        else:
            print(-1)