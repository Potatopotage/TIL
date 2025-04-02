"""
nCm
"""


import sys

input = sys.stdin.readline
n, m = map(int, input().split())

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

result = factorial(n) // (factorial(m) * factorial(n - m))

print(result)





"""
1192052400
"""