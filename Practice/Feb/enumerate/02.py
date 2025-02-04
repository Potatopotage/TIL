# 다음 리스트의 요소들을 1부터 시작하는 인덱스와 함께 출력하세요.

students = ["지민", "유진", "민수", "하영"]

# 출력 예시
# 1번째 학생: 지민  
# 2번째 학생: 유진  
# 3번째 학생: 민수  
# 4번째 학생: 하영  

for index, student in enumerate(students):
    print(f'{index + 1}번째 학생: {student}')
