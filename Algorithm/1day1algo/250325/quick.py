arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quicksort(arr, start, end):
    if start >= end:    #원소가 1개인 경우 종료
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # pivot보다 큰 데이터를 찾을 때까지 반복
        while arr[left] <= arr[pivot]:
            left += 1

        while arr[right] > arr[pivot]:
            right -= 1

        # 엇갈렸다면 right와 pivot 교체
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터 교체
        else:
            arr[left], arr[right] = arr[right], arr[left]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quicksort(arr, start, right - 1)
    quicksort(arr, right + 1, end)

quicksort(arr, 0, len(arr) - 1)
print(arr)