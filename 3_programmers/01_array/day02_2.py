# 문제 4 
# 수포자는 수학을 포기한 사람을 줄인 표현입니다. 
# 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 
# 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# 1번 수포자가 찍는 방식 : 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식 : 2, 1, 2, 3, 2, 4, 2, 5 ...
# 3번 수포자가 찍는 방식 : 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 ...
# 1번 문제부터 마지막 문제까지의 정답이 순서대로 저장된 배열 answers가 주어졌을 때 가장 많은 문제를 
# 맞힌 사람이 누구인지 배열에 담아 반환하도록 solution( ) 함수를 작성하세요.

answers = [1,2,3,4,5]

patterns = [
    [1, 2, 3, 4, 5], 
    [2, 1, 2, 3, 2, 4, 2, 5], 
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ] 

# 1. 정답과 일치 하면 해당 사람 score + 1

scores = [0] * 3

for i, answer in enumerate(answers):
    for j, pattern in enumerate(patterns):
        if answer == pattern[i % len(pattern)] :
            scores[j] += 1
            
# print("scores = " , scores)

# 2. max score 구하기

max_score = max(scores)

# print("max = ",max_score)

# 3. 가장 높은 점수를 가진 수포자들의 번호를 찾아서 리스트에 담음

highest_scores = []

for i, score in enumerate(scores):
    if score == max_score:
        highest_scores.append(i + 1)

# print(highest_scores)
        
    
    
def soultuin(answers):
    patterns = [
        [1, 2, 3, 4, 5], 
        [2, 1, 2, 3, 2, 4, 2, 5], 
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ] 
    
    # 1. 정답과 일치 하면 해당 사람 score + 1
    scores = [0] * 3

    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i % len(pattern)] :
                scores[j] += 1
                
    # 2. max score 구하기

    max_score = max(scores)
    
    # 3. 가장 높은 점수를 가진 수포자들의 번호를 찾아서 리스트에 담음

    highest_scores = []

    for i, score in enumerate(scores):
        if score == max_score:
            highest_scores.append(i + 1)
            
    return highest_scores