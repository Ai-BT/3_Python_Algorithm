# 문제 09 10진수를 2진수로 변환하기★
# 저자 권장 시간 _ 30분 | 권장 시간 복잡도 _ O(logN) | 출제 _ 저자 출제

# 10진수를 입력받아 2진수로 변환해 반환하는 solution( ) 함수를 구현하세요.

# 제약조건
# 제약 조건 없음

# 입출력의 예

# decimal 반환값
# 10 1010
# 27 11011

def solution(decimal):
    stack = []
    while decimal > 0:
        remainder = decimal % 2  # 나머지
        stack.append(str(remainder))
        decimal //= 2  # decimal = decimal // 2 # 몫
    binary = ""
    # 10진수 출력
    while stack:
        binary += stack.pop()

    return binary
