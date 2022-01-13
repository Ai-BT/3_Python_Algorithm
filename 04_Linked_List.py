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


# class Node: # 데이터, 주소 2가지 저장공간을 만들기 위해 class 사용
#     def __init__(self, data):
#         self.data = data
#         self.nets = None


class Node:
    # 생성자
    # self는 인스턴스(주소)를 자동으로 전달하는 것이다.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# 인스턴스 생성
node1 = Node(0)

# 인스턴스 할당
# 첫번째 head를 '0' 으로 할당
head = node1

# 링크드 리스트에 데이터 추가
def add(data):
    node = head # 첫 데이터를 node에 할당
    while node.next:
        node = node.next # None 이면, 끝남
    node.next = Node(data) # 인스턴스를 할당된 만큼 만들어 줌

# 데이터 for문 으로 추가
for index in range(1,10):
    add(index) # add 함수 9번 실행, 인자 전달

# 링크드 리스트 데이터 출력
node = head # 초기 위에서 할당된 0 을 가져옴


while node.next:
    print(node.data) # 8까지만 반복
    node = node.next # 9 까지 node 값이 할당 되고, while문 종료

print(node.data) #한번 더 출력해서 끝까지 데이터 출력



