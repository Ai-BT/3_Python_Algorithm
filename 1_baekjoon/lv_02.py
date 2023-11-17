# %%
# 1330

a, b = map(int, input().split())

if a > b:
    print(">")
elif a < b:
    print("<")
elif a == b:
    print("==")

# %%
# 14681

x = int(input())
y = int(input())

if x > 0 and y > 0:
    print("1")
elif x < 0 and y > 0:
    print("2")
elif x < 0 and y < 0:
    print("3")
elif x > 0 and y < 0:
    print("4")

# %%
# 2884

h, m = map(int, input().split())

if 0 <= h <= 23 and 0 <= m <= 59:
    if m > 44:
        print(h, m - 45)
    elif m < 45 and h > 0:
        print(h - 1, m + 15)
    else:
        print(23, m + 15)


# %%

# 2525
# 입력
# 첫째 줄에는 현재 시각이 나온다.
# 현재 시각은 시 A (0 ≤ A ≤ 23) 와 분 B (0 ≤ B ≤ 59)가 정수로 빈칸을 사이에 두고 순서대로 주어진다.
# 두 번째 줄에는 요리하는 데 필요한 시간 C (0 ≤ C ≤ 1,000)가 분 단위로 주어진다.

# 출력
# 첫째 줄에 종료되는 시각의 시와 분을 공백을 사이에 두고 출력한다.
# (단, 시는 0부터 23까지의 정수, 분은 0부터 59까지의 정수이다.
# 디지털 시계는 23시 59분에서 1분이 지나면 0시 0분이 된다.)

H, M = map(int, input().split())
timer = int(input())

H += timer // 60  # 몫
M += timer % 60  # 나머지

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24

print(H, M)


# %%
