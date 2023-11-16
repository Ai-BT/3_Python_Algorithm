# %%
# 1. 민지는 국제 포럼에서 아르바이트를 하게 되었습니다.
# 민지는 각 국에서 온 참가자들의 명단을 엑셀로 정리하고 있는데 참가자들 이름이 어떤 이는 전부 소문자,
# 어떤 이는 전부 대문자로 써져 있는 등 형식이 제각각이었습니다.
# 민지를 위해 이름이 입력되면 전부 대문자로 출력되는 프로그램을 만들어주세요.
# 입력 marry // 출력 MARY


def change(name):
    return name.upper()


change("marry")


# %%

# 2. 우리 태양계를 이루는 행성은 수성, 금성, 지구, 화성, 목성, 토성, 천왕성, 해왕성이 있습니다.
# 이 행성들의 영어 이름은
# Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune입니다.
# 행성의 한글 이름을 입력하면 영어 이름을 반환하는 프로그램을 만들어 주세요.

plates = {
    "수성": "Mercury",
    "금성": "Venus",
    "지구": "Earth",
    "화성": "Mars",
    "목성": "Jupiter",
    "토성": "Saturn",
    "천왕성": "Uranus",
    "해왕성": "Neptune",
}

name = input()
print(plates[name])


# %%

# 3. dict 만들기
# 첫 줄에는 학생의 이름이 공백으로 구분되어 입력되고,
# 두번째 줄에는 그 학생의 수학 점수가 공백으로 구분되어 주어집니다.
# 두 개를 합쳐 학생의 이름이 key이고 value가 수학 점수인 딕셔너리를 출력해주세요.
# 입력 Yujin Hyewon 70 100 // 출력 {'Yujin': 70, 'Hyewon': 100}


keys = input().split()
values = map(int, input().split())

result = dict(zip(keys, values))
print(result)


# 참고

# input().split()
# a, b = input('숫자 두 개를 입력하세요: ').split() # 입력받은 값을 공백을 기준으로 분리

# map(int, input().split())
# split의 결과를 매번 int로 변환해주려니 귀찮습니다.
# 이때는 map을 함께 사용하면 됩니다. map에 int와 input().split()을 넣으면
# split의 결과를 모두 int로 변환해줍니다(실수로 변환할 때는 int 대신 float를 넣습니다.).

# %%

# 4. 2-gram
# 2-gram이란 문자열에서 2개의 연속된 요소를 출력하는 방법입니다.
# 예를 들어 'Python'을 2-gram으로 반복해 본다면 다음과 같은 결과가 나옵니다.
# Py
# yt
# th
# ho
# on
# 입력으로 문자열이 주어지면 2-gram으로 출력하는 프로그램을 작성해 주세요.

text = input()

# 2-gram이므로 문자열의 끝에서 한 글자 앞까지만 반복함

for i in range(len(text) - 1):
    print(text[i], text[i + 1], sep="")


# %%

# 5. 대문자만 지나가세요
# 진구는 영어 학원 아르바이트를 하고 있습니다.
# 반 아이들은 알파벳을 공부하는 학생들인데 오늘은 대문자 쓰기 시험을 봤습니다.
# 알파벳 하나만을 입력하고 그 알파벳이 대문자이면 YES를 아니면 NO를 출력하는 프로그램을 만들어 주세요.
# → 알파벳 여러개를 입력하고 여러개 입력한 것 중 대문자만 출력해주는 프로그램도 만들어보세요.


text = "S"
texts = "dwdwdDSDSDSAsd"


def upper_method(eng):
    if eng.isupper() is True:
        print("yes")
    elif eng.isupper() is False:
        print("no")


texts.isupper()

list_text = list(texts)
for i in range(len(list_text)):
    if list_text[i].isupper() is True:
        print(list_text[i])

# %%

# 6. 문제30 : 문자열 속 문자 찾기
# 문자 pineapple에는 apple이라는 문자가 숨어 있습니다. 원범이는 이렇듯 문자열 속에 숨어있는 문자를 찾아보려고 합니다.

# 입력으로 첫 줄에 문자열이 주어지고 둘째 줄에 찾을 문자가 주어지면
# 그 문자가 시작하는 index를 반환하는 프로그램을 만들어 주세요

# 입력

# pineapple is yummy
# apple


# 출력
# 4

data = input()
word = input()

print(data.find(word))
