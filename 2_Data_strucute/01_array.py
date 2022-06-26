# 배열 (Array)
# 데이터를 나열하고, 각 데이터를 인덱스에 대응하도록 구성한 데이터 구조
# 파이썬에서는 리스트 타입이 배열 기능을 제공하고 있음

# 1. 배열이 왜 필요할까?
#   같은 종류의 데이터를 효율적으로 관리하게 위해 사용
#   같은 종류의 데이터를 순차적으로 저장
#   각각의 저장 공간을 인덱스 번호로 직접적으로 접근 가능

# 2. 배열의 장점, 단점
#   장점 - 빠른 접근이 가능, 어떤 저장공간 번호를 알면 알고 싶은 저장공간의 몇번째 위치인지 알 수 있음
#   단점 - 미리 데이터 저장공간을 설정 해줘야 한다. (ex 3개 공간에 추가로 2개를 넣어서 5개짜리로 만들지 못 한다.)
#   단점 - 데이터가 가변적이라면 별로다. (추가, 삭제가 불편하다)

# 3. 파이썬 배열
#   파이썬 리스트 활용

# 1차원 배열: 리스트로 구현


data_01 = [1,2,3,4,5]
print(data_01)

# 2차원 배열: 리스트로 구현
data_02 = [[1,2,3],[4,5,6],[7,8,9]]
print(data_02[0]) # 데이터 접근
print(data_02[2])
print(data_02[0][1])
print(data_02[2][2])

# 연습1: 위의 2차원 배열에서 9,8,7 순서로 출력해보기
print(data_02[2][2])
print(data_02[2][1])
print(data_02[2][0])

# %%

# 연습2: 다음 dataset 에서 전체 이름 안에 M이 몇번 나왔는지 빈도수 출력하기
dataset = ['Braund, Mr. Owen Harris',
'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
'Heikkinen, Miss. Laina',
'Futrelle, Mrs. Jacques Heath (Lily May Peel)',
'Allen, Mr. William Henry',
'Moran, Mr. James',
'McCarthy, Mr. Timothy J',
'Palsson, Master. Gosta Leonard',
'Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)',
'Nasser, Mrs. Nicholas (Adele Achem)',
'Sandstrom, Miss. Marguerite Rut',
'Bonnell, Miss. Elizabeth',
'Saundercock, Mr. William Henry',
'Andersson, Mr. Anders Johan',
'Vestrom, Miss. Hulda Amanda Adolfina',
'Hewlett, Mrs. (Mary D Kingcome) ',
'Rice, Master. Eugene',
'Williams, Mr. Charles Eugene',
'Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)',
'Masselmani, Mrs. Fatima',
'Fynney, Mr. Joseph J',
'Beesley, Mr. Lawrence',
'McGowan, Miss. Anna "Annie"',
'Sloper, Mr. William Thompson',
'Palsson, Miss. Torborg Danira',
'Asplund, Mrs. Carl Oscar (Selma Augusta Emilia Johansson)',
'Emir, Mr. Farred Chehab',
'Fortune, Mr. Charles Alexander',
'Dwyer, Miss. Ellen "Nellie"',
'Todoroff, Mr. Lalio']

m_count = 0
for data in dataset: # 하나씩 꺼냄
    # print(data)
    for index in range(len(data)): # 하나 꺼낸 배열을 더 작은 단위로 하나씩 꺼냄
        # print(data[index]) 
        if data[index] == 'M':
            m_count += 1

print('m_count = ',m_count)


test_dataset = ['12345678','abcde']
test_count = 0
for data in test_dataset:
    for index in range(len(data)):
        if data[index] == '3':
            test_count += 1

print('test_count = ',test_count)


# %%
