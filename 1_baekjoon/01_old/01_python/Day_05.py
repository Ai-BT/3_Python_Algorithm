# %%
# 서울의 오늘 날짜를 "YYYY-MM-DD" 형식으로 출력한다.

from datetime import datetime

now = datetime.now()

print(now.date())


# %%
# 2525
# 훈제오리구이를 시작하는 시각과 오븐구이를 하는 데 필요한 시간이 분단위로 주어졌을 때, 오븐구이가 끝나는 시각을 계산하는 프로그램을 작성하시오.
# 첫째 줄에는 현재 시각이 나온다. 현재 시각은 시 A (0 ≤ A ≤ 23) 와 분 B (0 ≤ B ≤ 59)가 정수로 빈칸을 사이에 두고 순서대로 주어진다.
# 두 번째 줄에는 요리하는 데 필요한 시간 C (0 ≤ C ≤ 1,000)가 분 단위로 주어진다.

# 입력
# 14 30
# 20

# 출력 14 50

H, M = map(int, input().split())
timer = int(input())

H += timer // 60
M += timer % 60

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24

print(H, M)


# %%

# 첫째 줄에는 현재 시각이 나온다. 현재 시각은 시 A (0 ≤ A ≤ 23), 분 B (0 ≤ B ≤ 59)와 초 C (0 ≤ C ≤ 59)가 정수로 빈칸을 사이에 두고 순서대로 주어진다.
# 두 번째 줄에는 요리하는 데 필요한 시간 D (0 ≤ D ≤ 500,000)가 초 단위로 주어진다.

# 14 30 0
# 200

# 14 33 20

H, M, S = map(int, input().split())
timer = int(input())

S += timer % 60
timer = timer // 60
if S >= 60:
    S -= 60
    M += 1

M += timer % 60
D = timer // 60
if M >= 60:
    M -= 60
    H += 1

H += D % 24
if H >= 24:
    H -= 24

print(H, M, S)

# %%
