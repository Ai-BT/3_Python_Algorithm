# 문제 3
# 정수 배열 numbers가 주어집니다.
# numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에
# 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

# 힌트
# 01단계 배열에서 두 수를 선택하는 모든 경우의 수를 구합니다.
# 02단계 과정 1에서 구한 수를 새로운 배열에 저장하고 중복값을 제거합니다.
# 03단계 배열을 오름차순으로 정렬하고 반환합니다.

number = [2, 1, 3, 4, 1]


def solution(number):
    ret = []
    for i in range(len(number)):
        for j in range(i+1, len(number)):
            ret.append(number[i] + number[j])
    result = sorted(set(ret))
    return result


print(solution(number))
