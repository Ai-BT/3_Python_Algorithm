# 문제 06 실패율★★
# 정답률 _ 60% | 저자 권장 시간 _ 60분 | 권장 시간 복잡도 _ O(M+NlogN) 출제 _ 2019 KAKAO BLIND RECRUITMENT

# 문제 URL

# 슈퍼 게임 개발자 오렐리는 큰 고민에 빠졌습니다. 그녀가 만든 프렌즈 오천성이 대성공을 거뒀지만 최근 신규 사용자 수가 급감했기 때문입니다.
# 원인은 신규 사용자와 기존 사용자 사이에 스테이지 차이가 너무 큰 것이 문제였습니다. 이 문제를 어떻게 할까 고민한 그녀는 동적으로 게임 시간을 늘려서 난이도를 조절하기로 했습니다.
# 역시 슈퍼 개발자라 대부분의 로직은 쉽게 구현했지만 실패율을 구하는 부분에서 위기에 빠지고 말았습니다. 오렐리를 위해 실패율을 구하는 코드를 완성하세요.

# 실패율 정의 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어의 수
# 전체 스테이지 개수가 N, 게임을 이용하는 사용자가 현재 멈춰 있는 스테이지의 번호가 담긴 배열 stages가 주어질 때
# 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨 있는 배열을 반환하도록 solution( ) 함수를 완성하세요.

# 제약조건
# 스테이지 개수 N은 1 이상 500 이하의 자연수입니다.
# stages의 길이는 1 이상 200,000 이하입니다.
# stages에는 1 이상 N + 1 이하의 자연수가 있습니다.
# 각 자연수는 사용자가 현재 도전 중인 스테이지 번호를 나타냅니다.
# 단, N + 1은 마지막 스테이지, 즉, N까지 클리어한 사용자를 나타냅니다.
# 만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오면 됩니다.
# 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0으로 정의합니다.

# 입출력의 예

# n     stages              result
# 5 [2,1,2,6,2,4,3,3]       [3,4,2,1,5]


# 첫번째 입출력 예를 보면 1번 스테이지에는 총 8명의 사용자가 도전했으며 이 중 1명의 사용자가 아직 클리어하지 못했습니다. 따라서 1번 스테이지의 실패율은 다음과 같습니다.

# 1번 스테이지 실패율 : 1/8
# 2번 스테이지에는 총 7명의 사용자가 도전했으며, 이 중 3명의 사용자가 아직 클리어하지 못했습니다. 따라서 2번 스테이지의 실패율은 다음과 같습니다.

# 2번 스테이지 실패율 : 3/7
# 마찬가지로 나머지 스테이지의 실패율은 다음과 같습니다.

# 3번 스테이지 실패율 : 2/4
# 4번 스테이지 실패율 : 1/2
# 5번 스테이지 실패율 : 0/1
# 각 스테이지의 번호를 실패율의 내림차순으로 정렬하면 다음과 같습니다.

# [3, 4, 2, 1, 5]

# --------------------------------------------------------------------------------------------- #

# stages 단계가 5 가 주어지고
# N의 유저가 마지막 스테이지 클리어를 표시
# result 값으로 실패율이 높은 순서대로 표시

N = 5  # 스테이지 수
stages = [2, 1, 2, 6, 2, 4, 3, 3]  # 마지막까지 클리어한 스테이지
result = []


def stage_fail(n, final_stages):
    for stage in range(n):
        for users, final_stage in enumerate(final_stages):
            users += 1
            if stage + 1 == final_stage:
                result.append(final_stage)


stage_fail(N, stages)
# print(result)

# --------------------------------------------------------------------------------------------- #


def solution(N, stages):
    # 1. 스테이지별 도전자 수를 구함

    #   N 번째 스테이지를 클리어하면 사용자의 스테이지는 N + 1
    #   인덱스는 0부터 시작이니깐 N + 2 로 설정
    #   첫번째 0 인덱스는 버리고, 1 인덱스부터가 stage
    #   N 스테이지를 클리어한 사람은 N + 1 로 넘어가기 때문에 마지막 하나가 더 필요
    challenger = [0] * (N + 2)

    for stage in stages:
        challenger[stage] += 1

    # 0 번째 인덱스는 버리고, 1 번째 인덱스가 stage 1
    # 각 stage 를 클리어한 유저 수 = challenger
    # print(challenger)

    # 2. 스테이지별 실패한 사용자 수 계산
    fails = {}
    total = len(stages)  # 총 유저 수

    # 3. 각 스테이지를 순회하며, 실패율 계산
    for i in range(1, N + 1):
        if challenger[i] == 0:  # ➍ 도전한 사람이 없는 경우, 실패율은 0
            fails[i] = 0
        else:
            fails[i] = challenger[i] / total  # ➎ 실패율 구함
            total -= challenger[i]  # ➏ 다음 스테이지 실패율을 구하기 위해
        #    현재 스테이지의 인원을 뺌

    # 4. 실패율이 높은 스테이지부터 내림차순으로 정렬
    result = sorted(fails, key=lambda x: fails[x], reverse=True)

    print(result)

    return result


solution(N, stages)
