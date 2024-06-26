from collections import deque
import time

# pop, popleft 성능 비교

lst = list(range(100000))
dq = deque(range(100000))

# pop(0) 성능 측정
start_time = time.time()
for i in range(100000):
    lst.pop(0)
print("pop(0) 소요시간: ", time.time() - start_time)

# popleft() 성능 측정
start_time = time.time()
for i in range(100000):
    dq.popleft()
print("deque의 popleft() 소요시간: ", time.time() - start_time)
