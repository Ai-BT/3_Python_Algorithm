
# 1. 큐 구조
# 가장 먼저 넣은 데이터를 가장 먼저 꺼낼 수 있는 구조
# 음식점에서 가장 먼저 줄을 선 사람이 제일 먼저 음식점을 입장하는 것
# FIFO (First in First out) 


# 2. 알아둘 용어
# Enqueue : 큐에 데이터를 넣는 기능
# Dequeue : 큐에서 데이터를 꺼내는 기능


# 3. 파이썬 queue 라이브러리 활용해서 큐 자료 구조 사용하기
# Queue() 
# LifoQueue()
# PrioriyQueue()

import queue

# Queue()
# 데이터 라이브러리 생성
data_queue = queue.Queue() # 라이브러리.클래스

data_queue.put('123') # 데이터 넣기
data_queue.put(1)

print(data_queue.qsize())
print(data_queue.get())
print(data_queue.qsize())

# %%

# LifoQueue()

data_queue = queue.LifoQueue()
data_queue.put('aasdd')
data_queue.put(12)

print(data_queue.qsize())
print(data_queue.get()) # 마지막에 넣은거 출력




# %%


# PrioriyQueue()
# 우선순위 큐

data_queue = queue.PriorityQueue()
data_queue.put((10, 'korea')) # 튜플로 넣어줌 (우선순위, 데이터)
data_queue.put((5, 1))
data_queue.put((15, 'china'))

print(data_queue.qsize())
print(data_queue.get())


# %%

# 연습 1 : 리스트 변수로 큐를 다루는 enqueue, dequeue 기능 구현

queue_list = list()

def enqueue(data):
    queue_list.append(data)

def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data

for index in range(10):
    enqueue(index)

print(len(queue_list))
print(dequeue())
print(dequeue())
    




# %%

