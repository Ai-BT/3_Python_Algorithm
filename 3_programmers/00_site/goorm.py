
# %%

# 1
# 문제 설명
# 정수와 더하기, 뺴기, 곱하기 기호로 이루어진 두 개의 수식 A, B가 주어진다.
# 주어지는 수식은 모두 올바른 수식이며, 구체적으로는 다음 조건들을 만족한다.
# 수식의 첫 문자와 마지막 문자는 항상 숫자이다.
# 수의 맨 첫 문자가 0인 경우는 없다. 예를 들어 031과 같은 수는 주어지지 않는다.
# 연산자가 최소 하나 이상 포함되어 있다.
# 연산자가 붙어서 등장하는 경우는 없다.
# 수식에 포함된 정수와 수식의 계산 결과는 모두 절댓값으로 1014 이하이다.
# 각 수식을 연산자 우선순위에 따라 계산했을 때, 두 수식의 계산 결과 중 더 큰 값을 출력하시오. 두 수식의 계산 결과는 항상 다름이 보장된다.

# 제한사항
# 첫째 줄에 수식 A, B가 공백을 두고 주어진다.
# 4수식은 숫자와 +, *, - 기호로만 이루어져 있다.
# 주어지는 수식의 길이는 3 이상 20 이하이다.
# 수식은 지문에서 주어진 조건을 항상 만족한다.

# 두 수식의 계산 결과 중 더 큰 값을 출력하시오.


# 입출력 예
# 입력 1
# 10+5 10+6

# 출력 1
# 16

# 입력 2
# 10*3-10 10*4-50

# 출력 2
# 20

# 입력 3
# 10*10-99 99-10*10

# 출력 3
# 1


user_input = input()
number_A, number_B = user_input.split()

result_A = eval(number_A)
result_B = eval(number_B)

print(max(result_A, result_B))

# %%

# 2
# 한 변의 길이가 N인 정사각형 모양의 격자판이 있다.
# 이 격자판의 각 격자는 길이가 1일 때, 이 격자판의 크고 작은 정사각형의 개수는 총 몇 개일까?
# 예를 들어 위 그림에서 보이는 한 변의 길이가 4인 정사각형 격자판에서 찾을 수 있는 크고 작은 정사각형은 총 30개이다.
# 이와 같이 정사각형 격자판의 한 변의 길이 N이 입력을 통해 주어질 때,
# 이 격자판에서 찾을 수 있는 모든 정사각형의 개수를 구하여라.

n = int(input())

result = 0
for i in range(1, n+1):
    sumNum = i**2
    result += sumNum

print(result)

# n = 1 1개
# n = 2 (4+1)
# n = 3 (9+4+1)

# %%
# https://tussle.tistory.com/1064

# 3
# N개의 10진수 정수가 주어진다. 플레이어에게 정수를 그냥 정렬하는 것은 너무 쉽기 때문에,
# 아래 기준에 따라 정수를 정렬하기로 한다.
# 1. 10진수 정수를 2진수로 나타냈을 때, 2진수에 포함된 1의 개수를 기준으로 내림차순 정렬한다.
# 2. 1의 개수가 같다면, 원래 10진수를 기준으로 내림차순 정렬한다.
# 플레이어가 정수를 잘 정렬했을 때, 앞에서 K번째에 위치한 수는 어떤 수가 될지 구해보자.

# 입력
# 첫째 줄에 주어지는 정수의 수 N과 플레이어가 찾으려는 정수의 위치 K가 공백을 두고 주어진다.


# N, K = map(int, input().split())
# alist = list(map(int, input().split()))

# print(N, K)
# print(alist)

# 예제 리스트
data = [1, 2, 3, 4, 5, 6, 7, 8]

print(data)

binary_data = [bin(x) for x in data]
print(binary_data)

binary_data_count = [bin(x).count('1') for x in data]
print(binary_data_count)


def check_bin(x):
    return bin(x).count('1')


# 정렬
# 1의 개수 내림차순, 같은 경우 숫자 자체 내림차순
# reverse = True 줘서 내림차순으로 변경
sorted_data = sorted(data, key=lambda x: (check_bin(x), x), reverse=True)

# 첫 번째 코드: 오직 check_bin(x)의 결과만을 기준으로 내림차순 정렬합니다.
# sorted(alist, key=lambda x: (check_bin(x)), reverse=True)

# 두 번째 코드: check_bin(x)의 결과를 첫 번째 기준으로, x 자체를 두 번째 기준으로 하여 내림차순 정렬합니다. 즉, check_bin(x)의 결과가 동일한 경우 x 자체로 내림차순 정렬합니다.
# sorted(alist, key=lambda x: (check_bin(x), x), reverse=True)


def check_bin(num):
    cnt_of_one = bin(num).count('1')
    return cnt_of_one


def pass_arr(arr, K):
    sorted_val = sorted(arr, key=lambda x: (check_bin(x), x), reverse=True)
    return sorted_val[K - 1]  # k 번째 숫자를 뽑기 위해서 [K - 1]


N, K = map(int, input().split())
S = list(map(int, input().split()))

result = pass_arr(S, K)
print(result)


# %%

# sorted 활용 예제
data_ex = [5, 3, 7, 10]

# 정렬 기준 함수


def square(x):
    return x * x


# sorted 함수로 정렬 (기본값은 오름차순)
sorted_data_ex = sorted(data_ex, key=square)

print(sorted_data_ex)  # 출력: [3, 5, 7, 10]


# lambda 이해 예제
def add(a, b):
    return a + b


# lambda 함수로 동일한 기능 구현
# add_lambda = lambda a, b: a + b


print(add(2, 3))       # 출력: 5
# print(add_lambda(2, 3))  # 출력: 5

# %%

# 4
# 문제 설명
# 구름이는 배열에 N개의 정수를 순서대로 넣으려고 한다.
# 이때 정수 중에서 숫자 문자열 K가 포함되어 있으면 배열에 넣지 않기로 한다. 정수는 순서대로 주어지며,
# i번째 제공되는 정수는 ai라고 한다.
# 이때 포함되어 있다는 의미는 정수에 숫자 문자열 K가 순서대로 정확히 있어야 한다.
# 모든 정수를 배열에 넣었을 때, 배열에 들어갈 수 있는 정수의 개수를 출력하시오.

# 제한사항
# 첫째 줄에 N과 K가 주어진다.
# 둘쨰 줄에 a1, a2, ..., aN이 공백을 두고 주어진다.
# 1 <= N <= 100000
# 1 <= K <= 100
# 1 <= ai <= 200000

# 배열에 들어갈 수 있는 정수의 개수를 출력하시오.


# 입출력 예
# 입력 1
# 5 2
# 10 20 22 12 11

# 출력 1
# 2

N, K = input().split()
alist = list(map(str, input().split()))

print(alist)

count = 0
for s in alist:
    if K not in s:
        count += 1

print(count)


# %%

# 5
# 문제 설명
# 구름스퀘어의 타운 홀은 다양한 행사를 진행할 수 있는 공간이다.
# 타운 홀에 N개의 행사가 예정되어 있다. i번째 행사는 시작 시간 si와 종료시간 ei까지 진행하려고 하고,
# 행사끼리 진행하는 시간이 서로 겹치지 않게 가장 많은 행사를 여는 것이 목표이다.
# 행사는 한 번 시작하면 중간에 종료할 수 없다. 그리고 행사가 종료된 후 바로 다음 행사를 진행할 수는 없고,
# 최소 1의 시간이 지난 뒤에 다른 행사가 시작할 수 있다. 행사의 시작 시간과 종료 시간이 동일한 경우도 있으며,
# 이는 시작하자마자 종료된 행사라고 할 수 있다.
# 타운 홀에서 열릴 수 있는 행사의 최대 개수를 출력하시오.

# 제한사항
# 첫째 줄에 행사의 개수 N이 주어진다.
# 다음 N개의 줄에는 i번쨰 행사의 시작 시간과 끝 시간을 나타내는 si, ei가 공백을 두고 주어진다.
# 1 <= N <= 200000
# 1 <= si <= ei <= 109
# 입력에서 주어지는 수는 모두 정수이다.

# 타운 홀에서 열 수 있는 행사의 최대 개수를 출력하시오.


# 입출력 예
# 입력 1
# 6
# 1 2
# 2 3
# 3 6
# 4 5
# 1 10
# 11 13

# 출력 1
# 3

# 입력 2
# 7
# 1 2
# 3 3
# 3 5
# 4 10
# 5 6
# 7 9
# 10 11

# 출력 2
# 5

schedule = [(3, 4), (1, 2), (5, 6), (1, 10), (2, 8)]


def max_events(schedule):
    schedule.sort(key=lambda x: x[1])  # 끝나는 시간을 기준으로 정렬
    print(schedule)
    last_end_time = -1
    count = 0

    for event in schedule:
        if event[0] > last_end_time:  # 이전 행사 종료 시간보다 시작 시간이 크면 (시간 겹치지 않음)
            count += 1
            last_end_time = event[1]

    return count


max_events(schedule)


# %%
def max_events(schedule):
    schedule.sort(key=lambda x: x[1])  # 끝나는 시간을 기준으로 정렬
    last_end_time = -1
    count = 0

    for event in schedule:
        if event[0] > last_end_time:  # 이전 행사 종료 시간보다 시작 시간이 크면 (시간 겹치지 않음)
            count += 1
            last_end_time = event[1]

    return count


N = int(input())
schedule = []
for _ in range(N):
    s, e = map(int, input().split())
    schedule.append((s, e))

result = max_events(schedule)
print(result)

# %%
