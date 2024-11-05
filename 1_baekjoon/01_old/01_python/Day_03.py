# %%
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

a = int(input())
b = int(input())

print(a + b)

# %%
# 문제 2588
# (세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
# (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.
# 2360
# 3776
# 1416
# 181720

a = int(input())
b = input()

result_1 = a * int(b[2])
result_2 = a * int(b[1])
result_3 = a * int(b[0])
result_4 = a * int(b)

print(result_1)
print(result_2)
print(result_3)
print(result_4)


# %%

# 3046번
# 두 수의 평균 S는 (R1+R2)/2
# 5분 후에 상근이는 생일 선물로 두 숫자 R1과 R2를 말해주어야 하지만, 안타깝게도 R2를 까먹고 말았다. 하지만 R1과 S는 기억하고 있다!
# 상근이를 도와 R2가 몇 인지 구하는 프로그램을 작성하시오.

r1, s = map(int, input().split())

r2 = (2 * s) - r1

print(r2)

# %%
