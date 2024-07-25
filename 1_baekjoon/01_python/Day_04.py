# %%
# 2163
# 초콜릿의 크기가 주어졌을 때, 이를 1×1 크기의 초콜릿으로 쪼개기 위한 최소 쪼개기 횟수를 구하는 프로그램을 작성하시오.

a, b = map(int, input().split())

result = (a * b) - 1
print(result)

# %%

# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.

T = int(input())

for i in range(1, T + 1):
    a, b = map(int, input().split())
    print("Case #" + str(i) + ":", (a + b))

# %%

# Case #1: 1 + 1 = 2

T = int(input())

for i in range(1, T + 1):
    a, b = map(int, input().split())
    print("Case #" + str(i) + ":", a, "+", b, "=", (a + b))

# %%
