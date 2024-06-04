
# 문제 15 요세푸스 문제
# N명의 사람이 원 형태로 서 있습니다. 각 사람은 1부터 N까지 번호표를 갖고 있습니다.
# 그리소 임의의 숫자 k가 주어졌을 때 다음과 같이 사람을 없앱니다.

# - 1번 번호표를 가진 사람을 기준으로 K 번째 사람을 없앱니다.
# - 없앤 사람 다음 사람을 기준으로 하고 다시 k 번째 사람을 없앱니다.

# n 과 k 가 주어질 떄 마지막에 살아있는 사람의 번호를 반환하는 함수를 구현해주세요.

# 입출력 예
# n k reture
# 5 2 3

from collections import deque


def solution(N, K):
    # ❶ 1부터 N까지의 번호를 deque에 추가
    queue = deque(range(1, N+1))

    while len(queue) > 1:  # ❷ deque에 하나의 요소가 남을 때까지
        for _ in range(K-1):
            queue.append(queue.popleft())  # ❸ K번째 요소를 찾기 위해 앞에서부터 제거하고 뒤에 추가
        queue.popleft()  # ❹ K번째 요소 제거
    return queue[0]  # ❺ 마지막으로 남은 요소 반환


print(solution(5, 2))
