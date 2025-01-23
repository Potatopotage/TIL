# 문제: 온라인 쇼핑몰 주문 데이터 검증
# 다음과 같은 주문 정보를 검증하는 함수를 작성하세요:
# order_id: 10자리 숫자여야 합니다.
# customer_email: '@'를 포함하고 '.com' 또는 '.net'으로 끝나야 합니다.
# product_name: 비어있지 않아야 하며 50자를 초과하지 않아야 합니다.
# quantity: 1에서 100 사이의 정수여야 합니다.
# price: 0보다 커야 하며 소수점 둘째 자리까지만 허용됩니다.
# order_date: 'YYYY-MM-DD' 형식이어야 하며, 현재 날짜보다 이후일 수 없습니다.
# 함수는 모든 조건을 만족하면 True를, 그렇지 않으면 False와 오류 메시지 리스트를 반환해야 합니다.
# 함수는 다음과 같은 형식의 딕셔너리를 입력받습니다:

order = {
    'order_id': '1234567890',
    'customer_email': 'customer@example.com',
    'product_name': 'Wireless Headphones',
    'quantity': 2,
    'price': 89.99,
    'order_date': '2025-01-15'
}
