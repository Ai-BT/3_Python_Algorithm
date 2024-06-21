# Day_04

# %%

# 1
# 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

# 제한 사항
# n은 0 이상 3000이하인 정수입니다.

# 입출력 예
# n	return
# 12	28
# 5	    6

def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if n % i == 0:
            answer += i
    return answer


# %%

# 2
# 자연수 N이 주어지면,
# N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
# 예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

# 제한사항
# N의 범위 : 100,000,000 이하의 자연수

# 입출력 예
# N	    answer
# 123	6
# 987	24

n = 987


def solution(n):
    answer = 0
    answer = sum(map(int, str(n)))

    return answer


solution(n)

# result = list(map(int, str(n)))
# print(result)


# %%

# 3
# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요.
# 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

# 제한 조건
# n은 10,000,000,000이하인 자연수입니다.
# 입출력 예
# n	    return
# 12345	[5,4,3,2,1]

n = 12345


def solution(n):

    answer = list(map(int, str(n)))
    answer.reverse()

    return answer


solution(n)

# %%

# 4

# 함수 solution은 정수 n을 매개변수로 입력받습니다.
# n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요.
# 예를들어 n이 118372면 873211을 리턴하면 됩니다.

# 제한 조건
# n은 1이상 8000000000 이하인 자연수입니다.

# 입출력   예
# n	    return
# 118372	873211


def solution(n):
    answer = list(str(n))
    answer.sort(reverse=True)

    answer = ''.join(answer)

    return int(answer)


n = 118372

solution(118372)


# %%

# 5
# 문제 설명
# 임의의 양의 정수 n에 대해,
# n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
# n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

# 제한 사항
# n은 1이상, 50000000000000 이하인 양의 정수입니다.

# 입출력 예
# n 	return
# 121	144
# 3	    -1


def solution(n):
    if int(n**0.5) == n**0.5:  # 제곱수 판별
        return ((n**0.5)+1)**2  # 제곱근+1의 제곱수 반환
    else:
        return -1  # 제곱수 아니면 -1반환


# %%

# 6
# 정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.

# 제한 조건
# num은 int 범위의 정수입니다.
# 0은 짝수입니다.

# 입출력 예
# num	return
# 3	"Odd"
# 4	"Even"

def solution(num):
    if num % 2 == 0:
        answer = "Even"
    else:
        answer = "Odd"
    return answer

# %%

# 7
# 정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

# 제한사항
# arr은 길이 1 이상, 100 이하인 배열입니다.
# arr의 원소는 -10,000 이상 10,000 이하인 정수입니다.

# 입출력 예
# arr	    return
# [1,2,3,4]	    2.5
# [5,5]	    5


arr = [5, 5]


def solution(arr):

    arr_sum = sum(arr)
    arr_avg = arr_sum/len(arr)

    return arr_avg


solution(arr)

# %%

# 8
# 양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다.
# 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다.
# 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

# 제한 조건
# x는 1 이상, 10000 이하인 정수입니다.

# 입출력 예
# x	    return
# 10	true
# 12	true
# 11	false
# 13	false


def solution(x):
    answer = True

    x_list = list(map(int, str(x)))
    x_sum = sum(x_list)

    if x % x_sum == 0:
        answer = True
    else:
        answer = False
    return answer


solution(18)


# %%

# 9
# 함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다.
# 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

# 제한 조건
# x는 -10000000 이상, 10000000 이하인 정수입니다.
# n은 1000 이하인 자연수입니다.

# 입출력 예
# x	    n	answer
# 2	    5	[2,4,6,8,10]
# 4	    3	[4,8,12]
# -4	2	[-4, -8]

x = -4
n = 2


def solution(x, n):
    answer = []

    for i in range(n):
        answer.append(x * (i + 1))

    return answer


solution(x, n)


# %%

# 10

# 문제 설명
# 자연수 n이 매개변수로 주어집니다.
# n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요.
# 답이 항상 존재함은 증명될 수 있습니다.

# 제한사항
# 3 ≤ n ≤ 1,000,000
# 입출력 예

# n	    result
# 10	3
# 12	11

n = 12


def solution(n):
    answer = 0
    num_list = []

    for i in range(n):
        if n % (i + 1) == 1:
            num_list.append(i+1)

    answer = min(num_list)

    return answer


solution(n)

# %%

# 11
