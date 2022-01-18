# Hash Table

# 1. 해쉬 구조
# Hash Table : 키(key) 데이터(value)를 저장하는 데이터 구조
#   - key를 통해 바로 데이터를 받아올 수 있으므로, 속도가 획기적으로 빨라짐
#   - 파이썬 딕셔너리 타입이 해쉬 테이블의 예
#   - 파이썬에서는 해쉬를 별도 구현할 이유가 없음 - 딕셔너리 타입을 사용하면 됨

# 2. 알아둘 용어
# 해쉬(hash): 임의 값을 고정 길이로 변환하는 것 (데이터를 고정길이로 변환하는 것)
# 해쉬 테이블 : 키 값의 연산에 의해 직접 접근이 가능한 데이터 구조
# 해싱 함수 : key에 대해 산술 연산을 이용해 데이터 위치를 찾을 수 있는 함수 
# 슬롯 : 한개의 데이터를 저장할 수 있는 공간

# 3. 간단한 해쉬 예
# 배열을 인덱스를 가지지만, 리스트는 그렇지 않다
# 하지만 파이썬 리스트는 왜 인덱스를 가질까?
# 파이썬의 리스트 내부는 배열처럼 구현되어 있다.
# 파이썬 리스트의 아이템들은 메모리 상의 연속적인 위치에 배치되며, 인덱스를 사용하여 접근이 가능하다.


# 1.
hash_table = list([0 for i in range(10)])

# 일종의 데이터를 저장할 수 있는 슬롯을 가지고 있고,
# 인덱스 번호를 각각 가지고 있으니,
# 일종의 해쉬주소와 각각의 슬롯이 연결된 해쉬 테이블이라고 할 수 있다.
print(hash_table) 
print('-------------------------')

# 2. 간단한 해쉬 함수
# 가장 간단한 방식이 Divsion 법
def hash_func(key):
    return key % 5

# 고정된 길이로 결과값이 나온다.
print(hash_func(999))
print('-------------------------')


# 3. 해쉬 테이블에 저장
# 각각의 매칭되는 키가 존재해야 한다.
data1 = 'Andy'
data2 = 'Dave'
data3 = 'Trump'

# ord() : 문자의 ASCII 코드를 리턴해주는 함수
# 아스키 코드값을 키값을 활용 A - 65, D- 68, T -84
print(ord(data1[0]), ord(data2[0]), ord(data3[0]))
print( ord(data1[0]), hash_func(ord(data1[0])) ) # 데이터, 키값(해쉬주소)


def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value


# 특정 주소의 데이터를 가져오는 함수
storage_data('Andy', '232314')
storage_data('Dave', '32425345')
storage_data('Trump', '200003')

# 데이터를 저장하고 읽기
def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]


# 결과
result = get_data('Trump')
print(result)







