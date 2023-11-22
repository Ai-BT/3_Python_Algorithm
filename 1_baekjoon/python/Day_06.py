# %%
# 2914
# 입력
# 38 24
# 첫째 줄에 앨범에 수록된 곡의 개수 A와 평균값 I가 주어진다. (1 ≤ A, I ≤ 100)

# 출력
# 875
# 첫째 줄에 적어도 몇 곡이 저작권이 있는 멜로디인지 출력한다.

# A 는 앨범의 수
# I 는 평균값

import math

A, I = map(int, input().split())

I = I - 0.99

X = I * A
print(math.ceil(X))

# %%
# 5355
# 화성에서는 지구와는 조금 다른 연산자 @, %, #을 사용한다. @는 3을 곱하고, %는 5를 더하며, #는 7을 빼는 연산자이다.
# 따라서, 화성에서는 수학 식의 가장 앞에 수가 하나 있고, 그 다음에는 연산자가 있다.
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 다음 줄에는 화성 수학식이 한 줄에 하나씩 주어진다

# 입력
# 3
# 3 @ %
# 10.4 # % @
# 8 #

# 출력
# 14.00
# 25.20
# 1.00

T = int(input())

for _ in range(T):
    mars = list(map(str, input().split()))
    answer = 0
    for i in range(len(mars)):
        if i == 0:
            answer += float(mars[i])
        else:
            if mars[i] == "@":
                answer *= 3
            elif mars[i] == "%":
                answer += 5
            elif mars[i] == "#":
                answer -= 7

    print(format(answer, ".2f"))


# %%
# 2675
# 문제
# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
# 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.
# QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다.
# S의 길이는 적어도 1이며, 20글자를 넘지 않는다.

# 출력
# 각 테스트 케이스에 대해 P를 출력한다.

# 예제
# 2
# 3 ABC    -->    AAABBBCCC
# 5 /HTP   -->    /////HHHHHTTTTTPPPPP

T = int(input())

for _ in range(T):
    R, S = map(str, input().split())
    for i in S:
        print(i * int(R), end="")  # end='' 옆으로 붙임
    print()

# %%
