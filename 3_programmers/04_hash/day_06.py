# 문제 18
# 두개의 수로 특정값 만들기

# n개의 양의 정수로 이루어진 리스트 arr 와 정수 target이 주어졌을 떄 이 중에서 합이 target 인
# 두 수가 arr 에 있는지 찾고, 있으면 True, 없으면 False를 반환하는 solution() 함수를 작성

# 입출력 예
# arr           target          return
# [1,2,3,4,8]   6               True
# [2,3,5,9]     10              False

arr = [1, 2, 3, 4, 8]
target = 6


def count_sort(arr, k):
    hashtable = [0] * (k + 1)

    for num in arr:
        if num <= k:
            hashtable[num] = 1

    return hashtable


def solution(arr, target):
    hashtable = count_sort(arr, target)

    for num in arr:
        complemnet = target - num
        if (
            complemnet != num
            and complemnet >= 0
            and complemnet <= target
            and hashtable[complemnet] == 1
        ):
            return True

    return False


print(solution(arr, target))
