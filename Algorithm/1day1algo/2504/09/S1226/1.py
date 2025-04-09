"""
0 길
1 벽
2 출발점
3 도착점

도달 가능 1
도달 불가능 0
"""
from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')

def maze(r, c):
    pass

N = 16
T = 10
for _ in range(1, T + 1):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    pprint(arr)
    break


"""
#1 1
#2 1
#3 1
#4 0
#5 1
#6 1
#7 0
#8 1
#9 1
#10 1
"""