"""
다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다
단, 배열의 특정한 인덱스가 연속해서 K번을 초과하여 더해질 수 없다
"""
import sys
sys.stdin = open('input.txt', 'r')

N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

num = 0
max_num = arr.pop(arr.index(max(arr)))
next_max = arr.pop(arr.index(max(arr)))

# while True:
#     for _ in range(K):
#         num += max_num
#         M -= 1
#         if M == 0:
#             break
#
#     num += next_max
#     M -= 1
#     if M == 0:
#         break
#
# print(num)

next_max_cnt = M % K
max_cnt = M - next_max_cnt

num += next_max_cnt * next_max
num += max_cnt * max_cnt
print(num)