# %%
# 문제 2935

# 입력
# 첫째 줄에 양의 정수 A가 주어진다.
# 둘째 줄에 연산자 + 또는 *가 주어진다.
# 셋째 줄에 양의 정수 B가 주어진다.
# A와 B는 모두 10의 제곱 형태이고, 길이는 최대 100자리이다.

# 출력
# 첫째 줄에 결과를 출력한다. 결과는 A+B 또는 A*B이며, 입력에서 주어지는 연산자에 의해 결정된다.

# 예제 입력 1
# 1000
# *
# 100

# 예제 출력 1
# 100000

A = int(input())
method = input()
B = int(input())

if method == "+":
    result = A + B
    print(result)
elif method == "*":
    result = A * B
    print(result)


# %%

# 10817
# 문제
# 세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 세 정수 A, B, C가 공백으로 구분되어 주어진다. (1 ≤ A, B, C ≤ 100)

# 출력
# 두 번째로 큰 정수를 출력한다.

# 예제 입력 1
# 20 30 10
# 예제 출력 1
# 20

num_list = list(map(int, input().split()))
num_list.sort()
print(num_list[1])


# %%

# 11653
# 문제
# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.

# 출력
# N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.

# 예제 입력 1
# 72
# 예제 출력 1
# 2
# 2
# 2
# 3
# 3

N = int(input())
m = 2
while N != 1:  # N과 m을 나눴을때 몫이 1이 되면 멈춤.
    if N % m == 0:
        print(m)
        N = N // m
    else:
        m += 1

# %%
