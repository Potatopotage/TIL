"""
1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고,
양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다.
한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다.
"""
from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

arr = []

for i in range(N):
    arr.append(i + 1)

result = []

K = K - 1
idx = K
result.append(arr.pop(idx))
while arr:
    idx = (idx + K) % len(arr)
    result.append(arr.pop(idx))

print("<" + ", ".join(map(str, result)) + ">")





# idx = idx + K
# print(arr)
# print(arr.pop(idx % len(arr)))

# idx = idx + K
# print(arr.pop(K))
#
# idx = idx + K
# print(arr)
# print(len(arr))
# print(K)




# print(arr.pop(K))
# K *= 2
# print(arr.pop(K))
# K *= 2
# print(K)
# print(len(arr))
# if K > len(arr) - 1:
#     print(len(arr))
#     print(K)
#     K = K - len(arr)
#     print(arr)
#     print(arr.pop(K))
#     # print(arr.pop(K))



# print(arr)


"""
<3, 6, 2, 7, 5, 1, 4>
"""