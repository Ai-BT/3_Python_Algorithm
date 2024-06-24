# Day 05

# %%

# 1 **
# 문제 설명
# 길이가 같은 두 1차원 정수 배열 a, b가 매개변수로 주어집니다. a와 b의 내적을 return 하도록 solution 함수를 완성해주세요.

# 이때, a와 b의 내적은 a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1] 입니다. (n은 a, b의 길이)

# 제한사항
# a, b의 길이는 1 이상 1,000 이하입니다.
# a, b의 모든 수는 -1,000 이상 1,000 이하입니다.

# 입출력 예
# a	        b	        result
# [1,2,3,4]	[-3,-1,0,2]	3
# [-1,0,1]	[1,0,-1]	-2

import math
import numpy as np

a = [1, 2, 3, 4]
b = [-3, -1, 0, 2]

result = np.dot(a, b)


def solution(a, b):
    answer = np.dot(a, b)
    return int(answer)


# %%

# 2 **
# 문제 설명
# 두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서,
# 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ left ≤ right ≤ 1,000

# 입출력 예
# left	right	result
# 13	17	    43
# 24	27	    52


def solution(left, right):
    answer = 0
    for i in range(left, right+1):  # left 부터 right까지 1씩 증가하는 for문
        now_count = 0  # 약수의 개수를 담기위한 변수
        for j in range(1, i+1):  # 1부터 i까지 증가하며 약수를 찾아냅니다.
            if i % j == 0:  # 나누어 떨어지는 수는 약수!
                now_count += 1  # 약수라면 개수를 증가시켜줍니다.

        if now_count % 2 == 0:  # 이제 개수가 홀수인지 짝수인지 판별하여
            answer += i  # 짝수라면 더해주고
        else:
            answer -= i  # 홀수라면 빼줍니다.

    return answer  # 끝!


answer = 0
for i in range(left, right + 1):
    now_count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            now_count += 1

    if now_count % 2 == 0:
        answer += i
    else:
        answer -= i


# %%

# 3 **
# 문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
# s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.

# 제한 사항
# str은 길이 1 이상인 문자열입니다.

# 입출력 예
# s     	return
# "Zbcdefg"	"gfedcbZ"

s = "Zbcdefg"


def solution(s):
    answer = list(sorted(s, reverse=True))
    answer = "".join(answer)
    return answer


solution(s)

# %%

# 4
# 새로 생긴 놀이기구는 인기가 매우 많아 줄이 끊이질 않습니다.
# 이 놀이기구의 원래 이용료는 price원 인데, 놀이기구를 N 번 째 이용한다면 원래 이용료의 N배를 받기로 하였습니다.
# 즉, 처음 이용료가 100이었다면 2번째에는 200, 3번째에는 300으로 요금이 인상됩니다.
# 놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return 하도록 solution 함수를 완성하세요.
# 단, 금액이 부족하지 않으면 0을 return 하세요.

# 제한사항
# 놀이기구의 이용료 price : 1 ≤ price ≤ 2,500, price는 자연수
# 처음 가지고 있던 금액 money : 1 ≤ money ≤ 1,000,000,000, money는 자연수
# 놀이기구의 이용 횟수 count : 1 ≤ count ≤ 2,500, count는 자연수

# 입출력 예
# price	money	count	result
# 3	    20	    4	    10


price = 3
money = 20
count = 2


def solution(price, money, count):
    answer = 0
    pay = 0  # 총 이용요금
    for i in range(count):
        total_price = price * (i+1)
        pay += total_price

    answer = pay - money

    if answer < 0:
        answer = 0

    return answer


solution(price, money, count)

# %%

# 5
# 문제 설명
# 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요.
# 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.

# 제한 사항
# s는 길이 1 이상, 길이 8 이하인 문자열입니다.
# s는 영문 알파벳 대소문자 또는 0부터 9까지 숫자로 이루어져 있습니다
# .
# 입출력 예
# s	        return
# "a234"	false
# "1234"	true


def solution(s):
    answer = True
    if len(s) == 4 or len(s) == 6:
        try:
            int(s)
            answer = True
        except:
            answer = False
    else:
        return False

    return answer


solution(s)

# %%

# 6 **
# 문제 설명
# 이 문제에는 표준 입력으로 두 개의 정수 n과 m이 주어집니다.
# 별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.

# 제한 조건
# n과 m은 각각 1000 이하인 자연수입니다.

# 예시
# 입력
# 5 3

# 출력
# *****
# *****
# *****

n = 5
m = 3

for i in range(m):
    for j in range(n):
        print("*", end='')
    print('')


# %%

# 7 **
# 문제 설명
# 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요.
# 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다.
# 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

# 제한 사항
# 두 수는 1이상 1000000이하의 자연수입니다.

# 입출력 예
# n	m	return
# 3	12	[3, 12]
# 2	5	[1, 10]


n = 3
m = 12

# 최대 공약수
math.gcd(n, m)

# 최소 공배수
math.lcm(n, m)


def solution_math(n, m):
    answer = []
    answer.append(math.gcd(n, m))
    answer.append(math.lcm(n, m))
    return answer


def solution(n, m):
    # 최대 공약수 구하기
    for i in range(min(n, m), 0, -1):
        if (n % i == 0) and (m % i == 0):
            a = i
            break
    # 최소 공배수 구하기
    for j in range(max(n, m), (n * m) + 1):
        if j % n == 0 and j % m == 0:
            b = j
            break

    return [a, b]


# %%

# 8 **
# 배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다.
# 이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다.
# 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다. 예를 들면,

# arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
# arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.
# 배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.

# 제한사항
# 배열 arr의 크기 : 1,000,000 이하의 자연수
# 배열 arr의 원소의 크기 : 0보다 크거나 같고 9보다 작거나 같은 정수

# 입출력 예
# arr	            answer
# [1,1,3,3,0,1,1]	[1,3,0,1]
# [4,4,4,3,3]	    [4,3]

arr = [1, 1, 3, 3, 0, 1, 1]

# arr = set(arr)

# list(arr)


def solution(arr):
    # 결과를 저장할 리스트
    result = []

    # 이전 값을 저장할 변수
    prev = None

    # 주어진 배열을 순회
    for num in arr:
        # 현재 숫자가 이전 숫자와 다를 때만 결과에 추가
        if num != prev:
            result.append(num)
            prev = num

    return result


solution(arr)


# %%

# 9 **
# 문제 설명
# 자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후,
# 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# n은 1 이상 100,000,000 이하인 자연수입니다.

# 입출력 예
# n	    result
# 45	7
# 125	229

n = 45


def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)  # 나머지
        n = n // 3  # 몫

    answer = int(tmp, 3)  # 3진법을 10진법 정수로 변환
    return answer


solution(n)


# %%

# 10
# 문제 설명
# S사에서는 각 부서에 필요한 물품을 지원해 주기 위해 부서별로 물품을 구매하는데 필요한 금액을 조사했습니다.
# 그러나, 전체 예산이 정해져 있기 때문에 모든 부서의 물품을 구매해 줄 수는 없습니다.
# 그래서 최대한 많은 부서의 물품을 구매해 줄 수 있도록 하려고 합니다.

# 물품을 구매해 줄 때는 각 부서가 신청한 금액만큼을 모두 지원해 줘야 합니다.
# 예를 들어 1,000원을 신청한 부서에는 정확히 1,000원을 지원해야 하며, 1,000원보다 적은 금액을 지원해 줄 수는 없습니다.

# 부서별로 신청한 금액이 들어있는 배열 d와 예산 budget이 매개변수로 주어질 때,
# 최대 몇 개의 부서에 물품을 지원할 수 있는지 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# d는 부서별로 신청한 금액이 들어있는 배열이며, 길이(전체 부서의 개수)는 1 이상 100 이하입니다.
# d의 각 원소는 부서별로 신청한 금액을 나타내며, 부서별 신청 금액은 1 이상 100,000 이하의 자연수입니다.
# budget은 예산을 나타내며, 1 이상 10,000,000 이하의 자연수입니다.

# 입출력 예
# d	            budget	result
# [1,3,2,5,4]	9	    3
# [2,2,3,3]	    10	    4


# 작은거 부터 더해서 budget 보다 크면 stop

d = [1, 3, 2, 5, 4]
budget = 9

# 작은거부터 sort
d.sort()
d

# %%
