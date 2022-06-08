# Stack
# 데이터를 제한적으로 접근할 수 있는 구조
# 가장 나중에 쌓은 데이터를 가정 먼저 빼낼 수 있는 데이터 구조
# LIFO - 쌓아 놓은 책을 하나씩 꺼낸다고 생각

# 1. 주요 기능
# push, pop

# 2. 스택 구조와 프로세스 스택

# 재귀 함수
def recursive(data):
    if data < 0:
        print("ended")
    else:
        print(data)
        recursive(data - 1) # stack 으로 출력 후 끝난 후 밑에 동작
        print("returnes", data)

recursive(4)

# %%

# 3. 자료 구조 스택의 장단점
# 장점 - 데이터 저장, 읽기 속도가 빠르다
# 단점 - 데이터 최대 갯수를 미리 정해야 한다 , 파이썬은 최대 1000번만 재귀함수가 호출된다.

# 4. 파이썬 리스트 기능에서 제공하는 메서드로 스택 사용해보기
data_stack = list()

data_stack.append(1)
data_stack.append(2)

print(data_stack)

data_stack.pop()


# %%

# 5. 연습1: 리스트 변수로 스택을 다루는 pop, push 기능 구현해보기(pop, push 함수 사용하지 않고 구현)

stack_list = list()

def push(data):
    stack_list.append(data)

def pop():
    data = stack_list[-1] # 맨 끝은 -1 로 가져 올 수 있다.
    del stack_list[-1]
    return data

for index in range(10):
    push(index)

pop()


# %%
