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
