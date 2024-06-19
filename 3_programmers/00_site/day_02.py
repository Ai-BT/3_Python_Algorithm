# Day_02

# %%

# 1
# 문자열 my_string과 정수 배열 index_list가 매개변수로 주어집니다.
# my_string의 index_list의 원소들에 해당하는 인덱스의 글자들을 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

# 입출력 예
# my_string 	index_list	    result
# "cvsgiorszzzmrpaqpe"	[16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]	"programmers"
# "zpiaz"	[1, 2, 0, 0, 3]	"pizza"

my_string = "zpiaz"
index_list = [1, 2, 0, 0, 3]


def solution(my_string, index_list):
    answer = ''
    for i in index_list:
        answer += my_string[i]
    return answer


solution(my_string, index_list)


# %%

# 2
# 정수 start_num와 end_num가 주어질 때,
# start_num부터 end_num까지의 숫자를 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

# 입출력 예
# start_num	end_num	result
# 3	10	[3, 4, 5, 6, 7, 8, 9, 10]

start_num = 3
end_num = 10


def solution(start_num, end_num):
    answer = []
    for i in range(start_num, end_num + 1):
        answer.append(i)

    return answer


def solution_2(start, end):
    return list(range(start, end + 1))


# solution(start_num, end_num)

solution_2(start_num, end_num)

# %%

# 3
# 정수 n과 문자열 control이 주어집니다.
# control은 "w", "a", "s", "d"의 4개의 문자로 이루어져 있으며,
# control의 앞에서부터 순서대로 문자에 따라 n의 값을 바꿉니다.

# "w" : n이 1 커집니다.
# "s" : n이 1 작아집니다.
# "d" : n이 10 커집니다.
# "a" : n이 10 작아집니다.
# 위 규칙에 따라 n을 바꿨을 때 가장 마지막에 나오는 n의 값을 return 하는 solution 함수를 완성해 주세요.

# 입출력 예
# n	    control	    result
# 0	"wsdawsdassw"	-1


def solution(n, control):
    answer = n

    for i in range(len(control)):
        if "w" == control[i]:
            answer += 1
        elif "s" == control[i]:
            answer -= 1
        elif "d" == control[i]:
            answer += 10
        elif "a" == control[i]:
            answer -= 10
        else:
            answer = "error"

    return answer


n = 0
control = "wsdawsdassw"


def solution_2(n, control):
    key = dict(zip(['w', 's', 'd', 'a'], [1, -1, 10, -10]))
    return n + sum([key[c] for c in control])


# 참고
key = dict(zip(['w', 's', 'd', 'a'], [1, -1, 10, -10]))  # zip 으로 dict 생성
value = [key[word] for word in control]  # key 값으로 value 를 가지고 온다
result = sum([key[word] for word in control])  # sum 으로 모든 값을 더 해준다
print(result)


# %%

# 4
# 정수 리스트 num_list가 주어질 때,
# 마지막 원소가 그전 원소보다 크면 마지막 원소에서 그전 원소를 뺀 값을
# 마지막 원소가 그전 원소보다 크지 않다면 마지막 원소를 두 배한 값을 추가하여
# return하도록 solution 함수를 완성해주세요.

# 입출력 예
# num_list	result
# [2, 1, 6]	[2, 1, 6, 5]
# [5, 2, 1, 7, 5]	[5, 2, 1, 7, 5, 10]

num_list = [5, 2, 1, 7, 5]


def solution(num_list):

    if num_list[-1] > num_list[-2]:
        append_num = num_list[-1] - num_list[-2]
        num_list.append(append_num)
    else:
        append_num = 2 * num_list[-1]
        num_list.append(append_num)

    return num_list


solution(num_list)

# %%

# 5
# 정수가 담긴 리스트 num_list가 주어집니다.
# num_list의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을 return하도록 solution 함수를 완성해주세요.

# 입출력 예
# num_list	result
# [3, 4, 5, 2, 1]	393
# [5, 7, 8, 3]	581

num_list = [5, 7, 8, 3]


def solution(num_list):
    answer = 0
    a = ""
    b = ""
    for _, num in enumerate(num_list):
        if num % 2 == 1:
            a += str(num)
        else:
            b += str(num)

    answer = int(a) + int(b)

    return answer


solution(num_list)


# %%

# 6
# 정수가 담긴 리스트 num_list가 주어질 때,
# 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성해주세요.

# num_list	result
# [3, 4, 5, 2, 1]	1
# [5, 7, 8, 3]	0


num_list = [3, 4, 5, 2, 1]


def solution(num_list):
    answer = 0
    multiply = 1
    add = 0

    for i in num_list:
        multiply *= i
        add += i

    if multiply < add*add:
        answer = 1
    else:
        answer = 0
    return answer


# %%

# 7
# 두 정수 a, b와 boolean 변수 flag가 매개변수로 주어질 때,
# flag가 true면 a + b를 false면 a - b를 return 하는 solution 함수를 작성해 주세요.

# 입출력 예
# a	    b	flag	result
# -4	7	true	3
# -4	7	false	-11


def solution(a, b, flag):
    answer = 0
    if flag == True:
        answer = a + b
    else:
        answer = a - b

    return answer


solution(-4, 7, True)

# %%

# 8
# 양의 정수 n이 매개변수로 주어질 때,
# n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return 하고
# n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 하는
# solution 함수를 작성해 주세요.

# 입출력 예
# n	    result
# 7	    16
# 10	220

n = 7


def solution(n):
    answer = 0

    if n % 2 == 1:  # n 의 홀,짝 구분
        for i in range(1, n+1):  # 1 이상 8 미만
            if i % 2 == 1:
                answer += i
    else:
        for i in range(1, n+1):
            if i % 2 == 0:
                answer += int(i*i)

    return answer


solution(n)

# %%

# 9
# 정수 number와 n, m이 주어집니다. number가 n의 배수이면서 m의 배수이면 1을 아니라면 0을 return하도록 solution 함수를 완성해주세요.

# 입출력 예
# number	n	m	result
# 60	2	3	1
# 55	10	5	0\

number = 55
n = 2
m = 3


def solution(number, n, m):
    answer = 0
    if number % n == 0 and number % m == 0:
        answer = 1
    else:
        answer = 0
    return answer


def solution_2(number, n, m):
    return 1 if number % n == 0 and number % m == 0 else 0


solution(number, n, m)

# %%

# 10
# 정수 num과 n이 매개 변수로 주어질 때,
# num이 n의 배수이면 1을 return n의 배수가 아니라면 0을 return하도록 solution 함수를 완성해주세요.

# 입출력 예
# num	n	result
# 98	2	1
# 34	3	0

num = 34
n = 3


def solution(num, n):
    answer = 0
    if num % n == 0:
        answer = 1
    else:
        answer = 0
    return answer

# %%
