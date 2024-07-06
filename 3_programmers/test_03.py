# %%
# 3
# N개의 10진수 정수가 주어진다. 플레이어에게 정수를 그냥 정렬하는 것은 너무 쉽기 때문에,
# 아래 기준에 따라 정수를 정렬하기로 한다.
# 1. 10진수 정수를 2진수로 나타냈을 때, 2진수에 포함된 1의 개수를 기준으로 내림차순 정렬한다.
# 2. 1의 개수가 같다면, 원래 10진수를 기준으로 내림차순 정렬한다.
# 플레이어가 정수를 잘 정렬했을 때, 앞에서 K번째에 위치한 수는 어떤 수가 될지 구해보자.

# 입력
# 첫째 줄에 주어지는 정수의 수 N과 플레이어가 찾으려는 정수 의 위치K가 공백을 두고 주어진다.

# 입력
# 8 6
# 1 2 3 4 5 6 7 8

# 출력
# 4

N, K = map(int, input().split())
alist = list(map(int, input().split()))

alist = [1,2,3,4,5,6,7,8]

def check_bin(x):
    return bin(x).count("1")

a = list(map(check_bin, alist))
a






# %%


# N, K = map(int, input().split())
# alist = list(map(int, input().split()))
K = 6
alist = [1, 2, 3, 4, 5, 6, 7, 8]


def check_bin(x):
    return bin(x).count('1')


# 정렬
# 1의 개수 내림차순, 같은 경우 숫자 자체 내림차순
# reverse = True 줘서 내림차순으로 변경
# x 는 여기서 alist
sorted_data = sorted(alist, key=lambda x: (check_bin(x), x), reverse=True)

print(sorted_data)
print(sorted_data[K-1])


# 첫 번째 코드: 오직 check_bin(x)의 결과만을 기준으로 내림차순 정렬합니다.
# sorted(alist, key=lambda x: (check_bin(x)), reverse=True)

# 두 번째 코드: check_bin(x)의 결과를 첫 번째 기준으로, x 자체를 두 번째 기준으로 하여 내림차순 정렬합니다. 즉, check_bin(x)의 결과가 동일한 경우 x 순 정렬합니다.
# sorted(alist, key=lambda x: (check_bin(x), x), reverse=True)자체로 내림차
