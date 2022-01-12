# 링크드 리스트
# 링크드 리스트를 처음부터 끝까지 구현 해보자

# 1. 링크트 리스트 구조
# 연결리스트 라고도 함
# 배열은 순차적으로 연결된 공간에 데이터를 나열하는 구조
# 배열의 최대 단점은 데이터가 일렬로 연결되어야 하는데, 그런 단점을 보완한 것이 링크트 리스트다.
# 즉, 미리 데이터 구조를 만들지 않고 데이터를 넣어도 된다.

# 링크드 리스트의 데이터 형태
# 데이터 + 다음 데이터를 가리키는 주소(Pointer) = 하나의 데이터 (노드 Node)
# 노드, 포인터 용어는 알아두자


# 2. 간단한 링크드 리스트 예
# 주소만 알면 데이터를 알 수 있다.


# %%

# class Node: # 데이터, 주소 2가지 저장공간을 만들기 위해 class 사용
#     def __init__(self, data):
#         self.data = data
#         self.nets = None

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# Node 와 Node 연결하기

node1 = Node(1)
node2 = None(2)
node1.next = node2
head = node1

# %%

# 링크드 리스트로 데이터 추가하기

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def add(data):
    node = head
    while node.next: # node next를 계속 가는 것
        node = node.next
    # Node 이면
    node.next = Node(data)

node1 = Node(1)
head = node1

for index in range(1, 10):
    add(index)


# 링크드 리스트 데이터 출력(검색하기)
node = head
while node.next:
    print(node.data)
    node = node.next

print(node.data)




# %%
