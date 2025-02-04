# 🔹 두 개의 집합을 결합하고, 특정 요소를 제거한 후, 존재하지 않는 요소를 삭제해도 에러가 나지 않도록 처리하세요.

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# 1) 두 집합을 합치기
set_sum = set1.union(set2)
print(set_sum)

# 2) 3을 제거

set_sum.remove(3)
print(set_sum)

# 3) 10을 삭제 (에러 없이 실행되도록)

set_sum.discard(10)