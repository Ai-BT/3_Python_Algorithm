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

# %%

schedule = [(3, 4), (1, 2), (5, 6), (1, 10), (2, 8)]


sort_schedule = sorted(schedule, key= lambda x: x[1])

print(sort_schedule)


count = 0
last_end_time = -1
for event in sort_schedule:
    print(event[0])
    if event[0] > last_end_time:
        count += 1
        last_end_time = event[1]
        
count
        



# %%

# 1. N 입력값
# 2. 행사 시간 리스트

# N = int(input())
# schedule = []
# for _ in range(N):
#     s, e = map(int, input().split())
#     schedule.append((s, e))

schedule = [(3, 4), (1, 2), (5, 6), (1, 10), (2, 8)]

# 3. 끝나는 시간을 기준으로 정렬
# sort 원본 리스트를 변경
# sorted 새로운 리스트를 생성, 원본 리스트는 그대로

sort_schedule = sorted(schedule, key=lambda x: x[1])  # 끝나는 시간을 기준으로 정렬


last_end_time = -1
count = 0

for event in sort_schedule:
    if event[0] > last_end_time:  # 이전 행사 종료 시간보다 시작 시간이 크면 (시간 겹치지 않음)
        count += 1
        last_end_time = event[1]

count


# %%
