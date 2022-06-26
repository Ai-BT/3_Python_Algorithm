# 5. 파이썬 객체지향 프로그래밍으로 리스트 구현하기


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        

# 링크드 리스트를 관리 할 수 있는 class management
class NodeMgmt:
    def __init__(self,data):
        self.head = Node(data) # 맨 앞의 노드 

    # 노드를 추가하는 함수 (맨 끝)
    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
        node.next = Node(data)


    # 전체 리스트를 출력하는 함수
    def desc(self):
        node = self.head
        while node:
            # print(node.data)
            node = node.next

linkedlist1 = NodeMgmt(0) # 인스턴스에 0 하나 넣어줌 
linkedlist1.desc()

for data in range(1,10):
    linkedlist1.add(data)

linkedlist1.desc()