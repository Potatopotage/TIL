"""
앞으로 이동
왼쪽으로 90도 회전
오른쪽으로 90도 회전

출발지에서 목적지까지 최소의 조작으로 이동
(최단거리x, 최소 리모컨 조작 횟수)

아빠가 벨 수 있는 최대 나무의 수가 주어졌을 때,
차윤이가 RC카를 목적지까지 이동시키기 위한 최소 조작 횟수를 구하라

항상 위를 바라보는 상태로 조작을 시작

G: RC카가 이동 가능한 땅
T: RC카가 이동이 불가능한 나무
X: 현재 RC카의 위치
Y: RC카를 이동시키고자 하는 위치
"""
from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')

def drive(r, c):
    pass

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    pprint(arr)
    break

"""
#1 7
#2 19
"""