# 두 개의 리스트가 주어졌을 때, 같은 인덱스의 요소를 곱한 값을 새로운 리스트로 반환하는 코드를 
# zip과 lambda를 사용하여 작성하시오.

list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

# 출력 예시
# [10, 40, 90, 160, 250]

pair = list(zip(list1, list2))


print([x * y for x, y in pair])

print(list(map(lambda x: x[0] * x[1], pair)))