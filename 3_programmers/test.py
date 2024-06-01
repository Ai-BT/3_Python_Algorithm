# 문제 4
# 수포자는 수학을 포기한 사람을 줄인 표현입니다.
# 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다.
# 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# 1번 수포자가 찍는 방식 : 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식 : 2, 1, 2, 3, 2, 4, 2, 5 ...
# 3번 수포자가 찍는 방식 : 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 ...
# 1번 문제부터 마지막 문제까지의 정답이 순서대로 저장된 배열 answers가 주어졌을 때 가장 많은 문제를
# 맞힌 사람이 누구인지 배열에 담아 반환하도록 solution( ) 함수를 작성하세요.

# answers = [1,2,3,4,5]
answers = [1, 3, 2, 4, 2]


patterns = [
    [1, 2, 3, 4, 5],
    [2, 1, 2, 3, 2, 4, 2, 5],
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
]

# 1. 답안과 제출한 정답이 일치하는지 확인

scores = [0] * 3

for i, answer in enumerate(answers):
    for j, pattern in enumerate(patterns):
        if answer == pattern[i % len(pattern)]:
            scores[j] += 1

print("socres = ", scores)

# 2. max score 구하기

max_score = max(scores)

print("max = ", max_score)

# 3. 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담기

highest_score = []

for i, score in enumerate(scores):
    if score == max_score:
        highest_score.append(i + 1)

print(highest_score)
