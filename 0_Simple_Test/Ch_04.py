# 1. 시간복잡도 (Big-O)
# 계산 복잡도 이론에서 시간 복잡도는 문제를 해결하는데 걸리는 시간과 입력의 함수 관계를 가리킨다
# 컴퓨터과학에서 알고리즘의 시간 복잡도는 입력을 나타내는 문자열 길이의 함수로서 작동하는 알고리즘을 취해 시간을 정량화하는 것이다.
# 알고리즘의 시간복잡도는 주로 빅-오(Big-O)표기법을 사용하여 나타낸다

# %%

# 2. 문자열을 입력받으면 단어의 갯수를 출력하는 프로그램을 작성해 주세요.
# 입력 : 안녕하세요. 저는 제주대학교 컴퓨터공학전공 혜림입니다.
# 출력 : 5

text = "안녕하세요. 저는 제주대학교 컴퓨터공학전공 혜림입니다."
print(len(text.split(" ")))
# %%

# 3. 키가 주어지면 순서대로 제대로 섰는지 확인하는 프로그램을 작성해보자.
# 입력 : 176 156 155 165 166 169
# 출력 : NO

tall = [176, 156, 155, 165, 166, 169]

list_a = list(tall.strip().split())
list_a = [int(i) for i in list_a]

if list_a != sorted(list_a):
    print("NO")

else:
    print("YES")


# %%

# 4. 2제곱, 3제곱, 4제곱을 할 수 있는 Factory 함수


def one(n):
    def two(value):
        sq = value**n
        return sq

    return two


a = one(2)
b = one(3)
c = one(4)
print(a(10))
print(b(10))
print(c(10))
# %%
