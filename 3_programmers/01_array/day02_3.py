# 문제
# 2차원 행렬 arr1과 arr2를 입력받아 arr1에 arr2를 곱한 결과를 반환하는 solution( ) 함수를 완성하세요.

# 제약조건
# 행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.
# 행렬 arr1, arr2의 데이터는 -10 이상 20 이하인 자연수입니다.
# 곱할 수 있는 배열만 주어집니다

# 1. 행렬 arr1, arr2 의 행과 열의 수를 구하기
# 2. 0 으로 구성된 곱한 배열의 초기화 행렬 만들기
# 3. 행의 for 문, 열의 for 문, c2 의 for 문
# 4. 빈 배열에 곱한 배열 넣기

arr1 = [[1, 4], [3, 2], [4, 1]]  # 3x2
arr2 = [[3, 3], [3, 3]]  # 2x2

# return
# [[15,15],[15,15],[15,15]]


def soultion(arr1, arr2):
    # 1. 행렬 arr1, arr2 의 행과 열의 수를 구하기
    r1, c1 = len(arr1), len(arr1[0])
    r2, c2 = len(arr2), len(arr2[0])

    # 2. 0 으로 구성된 곱한 배열의 초기화 행렬 만들기
    # 열을 구성하고 행을 늘려준다.
    ret = [[0] * c2 for _ in range(r1)]

    # 3. 행의 for 문, 열의 for 문, c2 의 for 문
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                ret[i][j] += arr1[i][k] * arr2[k][j]

    print(ret)
    return ret


soultion(arr1, arr2)
