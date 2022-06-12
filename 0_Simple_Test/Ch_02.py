# %%

# 1. 1부터 100까지 합 (for문 활용)

sum = 0
for i in range(1,101):
    sum += i
print(sum)

# %%

# 2. 다음 소스코드에서 클래스를 작성하여 게임 캐릭터의 능력치와 '파이어볼'이 출력되게 만드시오.
#**주어진 소스 코드를 수정해선 안됩니다.**

# 출력 예시
# 545 210 10
# 파이어볼

class Wizard:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor
        
    def attack(self):
        print("파이어볼")
    

x = Wizard(health=545, mana=210, armor=10)
print(x.health, x.mana, x.armor)
x.attack()

# %%

# self 스스로 메모리를 생성하여 전달하는 역할
class Foo01:
        def func1():
                print("function 1")
        def func2(self):
                print("function 2")

f = Foo01()

f.func2()
# 파이썬 메서드의 첫번째 인자로 항상 인스턴스가 전달 되기 때문에 발생하는 문제
# 인자가 없지만 하나를 받아서 error
# f.func1() 

# %%

# 파이썬의 클래스는 그 자체가 하나의 네임스페이스이기 때문에 인스터스 생성과 상관없이
# 클래스 내의 메소드를 직접 호출 할 수 있습니다.

class Foo02:
    def func1():
            print("function 1")

    def func2(self):
            print(id(self))
            print("function 2")

f = Foo02()

print( id(f)) 
f.func2()

# 위 코드는 func1 메서드를 호출했지만 앞서 인스턴스를 통해 메서드를 호출했던 것과는 달리 오류가 발생하지 않는 것을 확인할 수 있습니다. 
# 왜냐하면 인스턴스.메서드() 형태로 호출한 것과 달리 이번에는 클래스명.메서드() 형태로 호출했기 때문입니다.
Foo02.func1()


# %%

# 3. 우리 태양계를 이루고 있는 행성은 수성, 금성, 지구, 화성, 목성, 토성, 천왕성, 해왕성으로 총 8개 입니다. 
# 저희는 우리 태양계의 n번째 행성이 무엇인지 알고 싶습니다.
# 입력 1 // 출력 수성

def plate(n):
    plate_list = ["수성", "금성", "지구", "화성", "목성", "토성", "천왕성", "해왕성"]
    return plate_list[n-1]

result = plate(1)
print(result)

# %%

# 4. 영희는 친구와 게임을 하고 있습니다. 서로 돌아가며 랜덤으로 숫자를 하나 말하고 
# 그게 3의 배수이면 박수를 치고 아니면 그 숫자를 그대로 말하는 게임입니다.
# 입력 3 // 출력 짝짝짝
# 입력 2 // 출력 2

def game(n):
    if n%3 == 0:
        print("짝짝짝") 
    else :
        print(n)

game(1)


# %%

# 5. 신학기가 시작되고, 아이들이 돌아가면서 자기소개를 하기로 했습니다.
# 만약 입력으로 `김다정`이라는 이름이 주어지면
# 출력 = 안녕하세요. 저는 김다정입니다.

def hello(name):
    print("안녕하세요. 저는 " + name + "입니다") 

hello('김다정')


# %%

# 6. 로꾸거
# 입력 거꾸로 // 출력 로꾸꺼

word = '로꾸거'
revers_word = "".join(reversed(word))

print(revers_word)
print(word[::-1])

s = 'abcde'
print(s[3::-1]) # dcba
print(s[4::-1])  # edcba
print(s[::-1])  # edcba

# %%

# 7.
# 유주는 놀이공원 아르바이트 중입니다. 그런데 놀이기구마다 키 제한이 있습니다.
# 유주가 담당하는 놀이기구는 키가 150 이상만 탈 수 있습니다.

# 입력으로 키가 주어지면
# 키가 150이 이상이면 YES를 틀리면 NO를 출력하는 프로그램을 작성하세요.


def play(tall):
    if tall >= 150:
        print("Yes")
    elif tall < 150:
        print("No")

play(149)


# %%

# 8.
# 영하네 반은 국어, 수학, 영어 시험을 보았습니다. 영하는 친구들의 평균 점수를 구해주기로 했습니다.

# 공백으로 구분하여 세 과목의 점수가 주어지면
# 전체 평균 점수를 구하는 프로그램을 작성하세요. 단, 소숫점 자리는 모두 버립니다.

def score(kor, math, eng):
    avg = (kor + math + eng) / 3
    result = round(avg, 0)
    print(kor, math, eng, sep=" ")
    print(result)

score(94.2, 44, 20.44)

data = list(map(int, input().split()))
print(int(sum(data)/3))
 

# %%


# 첫 번째 매개변수로는 함수가 오고
# 두 번째 매개변수로는 반복 가능한 자료형(리스트, 튜플 등)이 옵니다

# map 함수의 반환 값은 map객체 이기 때문에 
# 해당 자료형을 list 혹은 tuple로 형 변환시켜주어야 합니다.


# 리스트에 값을 하나씩 더해서 새로운 리스트를 만드는 작업
myList = [1, 2, 3, 4, 5]

# for 반복문 이용
result1 = []
for val in myList:
    result1.append(val + 1)

print(f'result1 : {result1}')


# map 함수 이용
def add_one(n):
    return n + 1


result2 = list(map(add_one, myList))  # map반환을 list 로 변환
print(f'result2 : {result2}')


# %%

# 9. 공백으로 구분하여 두 숫자 a와 b가 주어지면, a의 b승을 구하는 프로그램을 작성하세요.

def math(a,b):
    return a**b

print(math(3,3))


n = list(map(int, input().split()))
print(n[0] ** n[1])


# %%

# 10. 공백으로 구분하여 두 숫자가 주어집니다.
# 첫번째 숫자로 두번째 숫자를 나누었을 때 그 몫과 나머지를 공백으로 구분하여 출력하세요

data = list(map(int, input().split()))

result = data[0] // data[1]
left = data[0] % data[1]

print(result, left)


# %%
