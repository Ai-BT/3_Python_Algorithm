# 6. 링크드 리스트 삭제

# a (address) -> b (address) -> c (adress)
# - a 데이터 삭제시, 헤드가 바뀌어야 한다.
# - c 데이터 삭제시, 앞에 노드의 주소 값을 None 으로 바꿔줘야 한다.
# - b 데이터 삭제시, a 주소값 변경 and b 데이터 삭제

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        

# 링크드 리스트를 관리 할 수 있는 class management
class NodeMgmt:
    def __init__(self,data):
        self.head = Node(data) # 맨 앞의 노드 

    # 1. 노드를 추가하는 함수 (맨 끝)
    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
        node.next = Node(data)


    # 2. 전체 리스트를 출력하는 함수
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    # 3. 삭제 함수
    def delete(self, data):
        # 3-1 링크드 리스트에 데이터가 없는 경우
        if self.head == '':
            print("해당 값을 가진 노드가 없습니다.")
            return
        
        # 3-2 헤드를 삭제하는 경우
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp

        # 3-3 중간 노드 삭제
        else:
            node = self.head
            while node.next: # None 일때 까지 계속 반복
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                else:
                    node = node.next
                

linkedlist1 = NodeMgmt(0) # 인스턴스에 0 하나 넣어줌
linkedlist1.desc()

# head 가 살아있는지 확인
print(linkedlist1.head)


# head를 지움(위에서 언급한 경우의 수 1)
linkedlist1.delete(0)
print(linkedlist1.head)
print('=======================')


print('--linkedlist2--')
# 다시 하나의 노드 생성
linkedlist2 = NodeMgmt(0) # 인스턴스에 0 하나 넣어줌
# linkedlist2.desc()

# 여러 노드를 더 추가
for data in range(1,10):
    linkedlist2.add(data)
linkedlist2.desc()


# 노드 중에 한개를 삭제
print('delete 4')
linkedlist2.delete(4)
linkedlist2.desc()

print('delete 9')
linkedlist2.delete(9)
linkedlist2.desc()

