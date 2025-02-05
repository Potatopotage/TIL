import ast

arr = ast.literal_eval((input()))

n = len(arr)

for i in range(n - 1, 0, - 1):
    for j in range(i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print(f'패스 ({n - i}) 후 : {arr}')